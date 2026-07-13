from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from datetime import datetime, date

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


    hour = datetime.now().hour



    active_game = None





    if hour == 10:


        active_game = Game.objects.filter(

            name="KING MORNING OPEN",

            is_active=True

        ).first()



    elif hour == 11:


        active_game = Game.objects.filter(

            name="KING MORNING CLOSE",

            is_active=True

        ).first()





    elif hour == 12:


        active_game = Game.objects.filter(

            name="KING AFTER OPEN",

            is_active=True

        ).first()





    elif hour == 13:


        active_game = Game.objects.filter(

            name="KING AFTER CLOSE",

            is_active=True

        ).first()





    elif hour == 14:


        active_game = Game.objects.filter(

            name="KING EVENING OPEN",

            is_active=True

        ).first()





    elif hour == 15:


        active_game = Game.objects.filter(

            name="KING EVENING CLOSE",

            is_active=True

        ).first()





    elif hour == 16:


        active_game = Game.objects.filter(

            name="KING NIGHT OPEN",

            is_active=True

        ).first()





    elif hour == 17:


        active_game = Game.objects.filter(

            name="KING NIGHT CLOSE",

            is_active=True

        ).first()











    # ==========================
    # TODAY RESULT
    # ==========================


    results = Result.objects.filter(

        result_date=today

    ).order_by(

        "-created_at"

    )








    # ==========================
    # USER BETS
    # ==========================


    bets = ContestEntry.objects.filter(

        player=request.user

    ).order_by(

        "-id"

    )







    return render(

        request,


        "dashboard/dashboard.html",


        {


            "wallet":wallet,


            "active_game":active_game,


            "results":results,


            "bets":bets,


        }

    )