from django.urls import path


from .views import (
    recharge_request,
    payment_submit,
    wallet_page,
    admin_recharge_list,
    approve_recharge,
    withdraw,
    approve_withdraw,
    reject_withdraw,
)



urlpatterns = [
    
    path(
        "admin/recharge/",
        admin_recharge_list,
        name="admin_recharge_list"
    ),

    path(
        "recharge/",
        recharge_request,
        name="recharge_request"
    ),


    path(
        "payment-submit/",
        payment_submit,
        name="payment_submit"
    ),


    path(
        "wallet/",
        wallet_page,
        name="wallet_page"
    ),


    path(
        "admin/recharge/",
        admin_recharge_list,
        name="admin_recharge_list"
    ),


    path(
        "admin/recharge/approve/<int:recharge_id>/",
        approve_recharge,
        name="approve_recharge"
    ),
    
    path(

        "withdraw/",

        withdraw,

        name="withdraw"

    ),
    
   path(
    "approve-withdraw/<int:id>/",
    approve_withdraw,
    name="approve_withdraw"
),


path(
"reject-withdraw/<int:id>/",
reject_withdraw,
name="reject_withdraw"
),




]
