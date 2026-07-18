from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from games.models import Game, Result, ContestEntry
from wallet.models import Wallet


# =========================
# DASHBOARD
# =========================

@login_required
def dashboard(request):

    current_time = timezone.localtime().time()

    active_game = Game.objects.filter(
        open_time__lte=current_time,
        close_time__gt=current_time,
        is_active=True
    ).first()

    results = Result.objects.all().order_by("-created_at")

    wallet, created = Wallet.objects.get_or_create(
        user=request.user
    )

    context = {
        "active_game": active_game,
        "results": results,
        "wallet": wallet,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )


# =========================
# PLAY GAME
# =========================

@login_required
def game_play(request, game_id):

    game = get_object_or_404(
        Game,
        id=game_id,
        is_active=True
    )

    wallet, created = Wallet.objects.get_or_create(
        user=request.user
    )

    # ==========================
    # BET CLOSE (LAST 5 MINUTES)
    # ==========================

    from django.utils import timezone
    from datetime import datetime, timedelta

    current_time = timezone.localtime().time()

    game_close = datetime.combine(
        timezone.localdate(),
        game.close_time
    )

    bet_close = (
        game_close - timedelta(minutes=5)
    ).time()

    if current_time >= bet_close:

        messages.error(
            request,
            "Betting is closed for this game."
        )

        return redirect("dashboard")

    # ==========================
    # SAVE BET
    # ==========================

    if request.method == "POST":

        bets = request.POST.getlist("bets")

        if not bets:

            messages.error(
                request,
                "Please select at least one bet."
            )

            return redirect(
                "game_play",
                game_id=game.id
            )

        total_amount = 0

        for bet in bets:

            data = bet.split(",")

            total_amount += float(data[2])

        # ==========================
        # WALLET CHECK
        # ==========================

        if wallet.balance < total_amount:

            messages.error(
                request,
                "Insufficient wallet balance."
            )

            return redirect("recharge_request")

        # ==========================
        # DEDUCT BALANCE
        # ==========================

        wallet.balance -= total_amount
        wallet.save()

        # ==========================
        # SAVE BETS
        # ==========================

        for bet in bets:

            data = bet.split(",")

            ContestEntry.objects.create(

                player=request.user,

                game=game,

                entry_type=data[0],

                selected_number=data[1],

                amount=data[2],

                possible_win=0,

                payment_status="SUCCESS"

            )

        messages.success(
            request,
            "Bet Placed Successfully."
        )

        return redirect("dashboard")

    return render(
        request,
        "games/game_play.html",
        {
            "game": game,
            "wallet": wallet,
        }
    )
# =========================
# PAYMENT PAGE
# =========================

@login_required
def payment_page(request, entry_id):

    entry = get_object_or_404(
        ContestEntry,
        id=entry_id
    )

    upi_link = (
        f"upi://pay?"
        f"pa=9359085383@ybl"
        f"&pn=King Market"
        f"&am={entry.amount}"
        f"&cu=INR"
    )

    return render(
        request,
        "games/payment.html",
        {
            "entry": entry,
            "upi_link": upi_link
        }
    )