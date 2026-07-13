from django.urls import path
from .views import transaction_report

from .views import winning_report
from .views import (
    admin_dashboard,
    recharge_list,
    users_list,
    games_list,
    bets_list,
    results_list,
    add_result,
    bank_accounts,
    admin_bank_account,
    withdraw_requests
)

urlpatterns = [
    
    path(

    "winning-report/",

    winning_report,

    name="winning_report"

),
    
    path(
    "transaction-report/",
    transaction_report,
    name="transaction_report"
),


    path(
        "",
        admin_dashboard,
        name="admin_dashboard"
    ),


    path(
        "recharge/",
        recharge_list,
        name="recharge_list"
    ),


    path(
        "users/",
        users_list,
        name="users_list"
    ),


    path(
        "games/",
        games_list,
        name="games_list"
    ),


    path(
        "bets/",
        bets_list,
        name="bets_list"
    ),


    path(
        "results/",
        results_list,
        name="results_list"
    ),


    path(
        "results/add/",
        add_result,
        name="add_result"
    ),


    path(
        "bank-accounts/",
        bank_accounts,
        name="bank_accounts"
    ),
    
    path(
    "admin-bank-account/",
    admin_bank_account,
    name="admin_bank_account"
),
    path(
    "withdraw-requests/",
    withdraw_requests,
    name="withdraw_requests"
),


]