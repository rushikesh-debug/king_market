from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import date

from games.models import Game, Result, ContestEntry
from wallet.models import Wallet


@login_required
def dashboard(request):

    # ==========================
    # AUTO DELETE OLD DATA
    # ==========================

    today = date.today()

    # Delete previous day bets
    ContestEntry.objects.filter(
        created_at__date__lt=today
    ).delete()

    # Delete previous day results
    Result.objects.filter(
        result_date__lt=today
    ).delete()

    # ==========================
    # WALLET
    # ==========================

    wallet, created = Wallet.objects.get_or_create(
        user=request.user
    )

    # ==========================
    # ACTIVE GAME
    # ==========================

    current_time = timezone.localtime().time()

    active_game = Game.objects.filter(
        open_time__lte=current_time,
        close_time__gt=current_time,
        is_active=True
    ).first()

    # ==========================
    # TODAY RESULT
    # ==========================

    results = Result.objects.filter(
        result_date=today
    ).order_by("-created_at")

    # ==========================
    # USER BETS
    # ==========================

    bets = ContestEntry.objects.filter(
        player=request.user
    ).order_by("-id")

    # ==========================
    # RENDER
    # ==========================

    return render(
        request,
        "dashboard/dashboard.html",
        {
            "wallet": wallet,
            "active_game": active_game,
            "results": results,
            "bets": bets,
        }
    )