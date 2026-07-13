from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from games.models import Game, Result, ContestEntry
from wallet.models import Wallet



# =========================
# DASHBOARD
# =========================

@login_required
def dashboard(request):

    games = Game.objects.filter(
        is_active=True
    )


    results = Result.objects.all().order_by(
        '-published_at'
    )



    wallet, created = Wallet.objects.get_or_create(
        user=request.user
    )



    context = {

        "latest_games": games,

        "results": results,

        "wallet": wallet

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

        id=game_id

    )



    wallet, created = Wallet.objects.get_or_create(

        user=request.user

    )




    if request.method == "POST":



        bets = request.POST.getlist(
            "bets"
        )



        if not bets:


            messages.error(

                request,

                "Please select bet"

            )


            return redirect(
                "game_play",
                game_id
            )





        total_amount = 0



        # calculate total bet amount

        for b in bets:


            data = b.split(",")


            amount = int(
                data[2]
            )


            total_amount += amount





        # wallet check


        if wallet.balance < total_amount:



            messages.error(

                request,

                "Insufficient Wallet Balance Please Recharge"

            )


            return redirect(

                "recharge_request"

            )







        # deduct money


        wallet.balance -= total_amount

        wallet.save()





        # save bet


        for b in bets:



            data = b.split(",")



            ContestEntry.objects.create(

    user=request.user,

    game=game,

    amount=data[2]

)


            



        messages.success(

            request,

            "Bet Placed Successfully"

        )



        return redirect(

            "dashboard"

        )






    return render(

        request,

        "games/game_play.html",

        {

            "game":game,

            "wallet":wallet

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

            "entry":entry,

            "upi_link":upi_link

        }

    )