
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from django.contrib.auth import get_user_model


from accounts.models import BankAccount

from wallet.models import (
    RechargeRequest,
    Withdraw
)

from games.models import (
    Game,
    Result,
    ContestEntry,
    
)


from .models import AdminBankAccount



User = get_user_model()



# =========================
# ADMIN DASHBOARD
# =========================

from django.utils import timezone

def admin_dashboard(request):
    raise Exception("ADMIN DASHBOARD TEST")

    current_time = timezone.localtime().time()

    active_game = Game.objects.filter(
        is_active=True,
        open_time__lte=current_time,
        close_time__gte=current_time
    ).first()

    users = User.objects.count()

    games = Game.objects.count()

    bets = ContestEntry.objects.count()

    recharges = RechargeRequest.objects.all().order_by(
        "-created_at"
    )

    withdraw_requests = Withdraw.objects.all().order_by(
        "-created_at"
    )

    results = Result.objects.all().order_by(
        "-created_at"
    )

    single_summary = ContestEntry.objects.filter(
        entry_type="SINGLE"
    ).values(
        "selected_number"
    ).annotate(
        total=Sum("amount")
    )

    jodi_summary = ContestEntry.objects.filter(
        entry_type="JODI"
    ).values(
        "selected_number"
    ).annotate(
        total=Sum("amount")
    )

    pana_summary = ContestEntry.objects.filter(
        entry_type="PANA"
    ).values(
        "selected_number"
    ).annotate(
        total=Sum("amount")
    )

    context = {

        "users_count": users,

        "games_count": games,

        "bets_count": bets,

        "active_game": active_game,

        "recharges": recharges,

        "withdraw_requests": withdraw_requests,

        "results": results,

        "single_summary": single_summary,

        "jodi_summary": jodi_summary,

        "pana_summary": pana_summary,

    }

    return render(

        request,

        "adminpanel/dashboard.html",

        context

    )


# =========================
# ADD RESULT
# =========================

# =========================
# ADD RESULT
# =========================

def add_result(request):


    if request.method == "POST":


        game = get_object_or_404(

            Game,

            id=request.POST.get("game")

        )



        result_date = request.POST.get(
            "result_date"
        )


        publish_time = request.POST.get(
            "publish_time"
        )



        open_pana = request.POST.get(
            "open_pana"
        )


        open_single = request.POST.get(
            "open_single"
        )



        close_pana = request.POST.get(
            "close_pana"
        )


        close_single = request.POST.get(
            "close_single"
        )



        jodi = request.POST.get(
            "jodi"
        )




        result, created = Result.objects.get_or_create(


            game=game,


            result_date=result_date


        )



        # RESULT DATA


        result.open_pana = open_pana


        result.open_single = open_single



        result.close_pana = close_pana


        result.close_single = close_single



        result.jodi = jodi



        # ⏰ RESULT PUBLISH TIME


        if publish_time:

            result.publish_time = publish_time




        result.save()





        messages.success(

            request,

            "Result Saved Successfully"

        )



        return redirect(

            "admin_dashboard"

        )




    return redirect(

        "admin_dashboard"

    )


# =========================
# USERS
# =========================


def users_list(request):


    return render(

        request,

        "adminpanel/users.html",

        {

            "users":User.objects.all()

        }

    )







# =========================
# GAMES
# =========================


def games_list(request):


    return render(

        request,

        "adminpanel/games.html",

        {

            "games":Game.objects.all()

        }

    )







# =========================
# BETS
# =========================


def bets_list(request):


    return render(

        request,

        "adminpanel/bets.html",

        {

            "bets":ContestEntry.objects.all()

        }

    )







# =========================
# RESULTS
# =========================


def results_list(request):


    results = Result.objects.all().order_by(

        "-created_at"

    )


    return render(

        request,

        "adminpanel/results.html",

        {

            "results":results

        }

    )







# =========================
# RECHARGE
# =========================


def recharge_list(request):


    requests = RechargeRequest.objects.all().order_by(

        "-created_at"

    )


    return render(

        request,

        "adminpanel/recharge.html",

        {

            "requests":requests

        }

    )







# =========================
# BANK ACCOUNTS
# =========================


def bank_accounts(request):


    accounts = BankAccount.objects.all()


    return render(

        request,

        "adminpanel/bank_accounts.html",

        {

            "accounts":accounts

        }

    )







# =========================
# ADMIN BANK ACCOUNT
# =========================


def admin_bank_account(request):


    account = AdminBankAccount.objects.first()



    if request.method == "POST":



        AdminBankAccount.objects.update_or_create(

            id=1,

            defaults={


                "account_holder":

                request.POST.get(
                    "account_holder"
                ),



                "bank_name":

                request.POST.get(
                    "bank_name"
                ),



                "account_number":

                request.POST.get(
                    "account_number"
                ),



                "ifsc":

                request.POST.get(
                    "ifsc"
                ),



                "upi_id":

                request.POST.get(
                    "upi_id"
                ),


            }

        )


        return redirect(

            "admin_bank_account"

        )




    return render(

        request,

        "adminpanel/admin_bank_account.html",

        {

            "account":account

        }

    )







# =========================
# WITHDRAW REQUESTS
# =========================


def withdraw_requests(request):


    withdraws = Withdraw.objects.all().order_by(

        "-created_at"

    )


    return render(

        request,

        "adminpanel/withdraw_requests.html",

        {

            "withdraws":withdraws

        }

    )
    
    # =========================
# ADMIN TRANSACTION REPORT
# =========================

from wallet.models import WalletTransaction


def transaction_report(request):


    transactions = WalletTransaction.objects.all().order_by(
        "-created_at"
    )


    return render(

        request,

        "adminpanel/transaction_report.html",

        {
            "transactions": transactions
        }

    )
    
    # =========================
# ADMIN WINNING REPORT
# =========================

from wallet.models import WalletTransaction


def winning_report(request):


    winnings = WalletTransaction.objects.filter(

        transaction_type="WINNING"

    ).order_by(

        "-created_at"

    )



    return render(

        request,

        "adminpanel/winning_report.html",

        {

            "winnings": winnings

        }

    )
    
    