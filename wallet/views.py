from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal

from .models import (
    RechargeRequest,
    Wallet,
    Withdraw,
    Notification,
    WalletTransaction
)

import qrcode
import io
import base64

# =========================
# ADMIN RECHARGE LIST
# =========================

@login_required
def admin_recharge_list(request):

    requests = RechargeRequest.objects.all().order_by(
        "-created_at"
    )


    return render(

        request,

        "wallet/admin_recharge.html",

        {
            "requests":requests
        }

    )



# =========================
# RECHARGE PAGE
# =========================

@login_required
def recharge_request(request):


    if request.method == "POST":

        amount = request.POST.get("amount")


        upi_link = (
            f"upi://pay?"
            f"pa=9359085383@ybl"
            f"&pn=Rushikesh"
            f"&am={amount}"
            f"&cu=INR"
        )


        qr = qrcode.make(upi_link)


        buffer = io.BytesIO()

        qr.save(
            buffer,
            format="PNG"
        )


        qr_image = base64.b64encode(
            buffer.getvalue()
        ).decode()



        return render(
            request,
            "wallet/payment.html",
            {
                "amount":amount,
                "qr_image":qr_image
            }
        )



    return render(
        request,
        "wallet/recharge.html"
    )





# =========================
# PAYMENT SUBMIT
# =========================

# =========================
# PAYMENT SUBMIT
# =========================

@login_required
def payment_submit(request):


    if request.method == "POST":


        amount = request.POST.get(
            "amount"
        )



        RechargeRequest.objects.create(

            user=request.user,

            amount=amount,

            status="PENDING"

        )



        Notification.objects.create(

            user=request.user,

            message=
            f"Recharge request of ₹{amount} submitted successfully. Waiting for admin approval."

        )



        messages.success(

            request,

            "Payment Submitted Successfully"

        )



        return redirect(

            "dashboard"

        )



    return redirect(

        "recharge_request"

    )

# =========================
# ADMIN APPROVE RECHARGE
# =========================

@login_required
def approve_recharge(request,recharge_id):


    recharge=get_object_or_404(

        RechargeRequest,

        id=recharge_id

    )



    if recharge.status=="SUCCESS":

        return redirect(
            "admin_recharge_list"
        )



    wallet,created=Wallet.objects.get_or_create(

        user=recharge.user

    )



    wallet.balance += recharge.amount

    wallet.save()



    WalletTransaction.objects.create(

        user=recharge.user,

        transaction_type="RECHARGE",

        amount=recharge.amount,

        balance_after=wallet.balance

    )



    recharge.status="SUCCESS"

    recharge.save()



    Notification.objects.create(

        user=recharge.user,

        message=f"₹{recharge.amount} recharge added to wallet."

    )



    return redirect(
        "admin_recharge_list"
    )







# =========================
# USER WALLET
# =========================


@login_required
def wallet_page(request):


    wallet,created=Wallet.objects.get_or_create(

        user=request.user

    )



    transactions=WalletTransaction.objects.filter(

        user=request.user

    ).order_by(

        "-created_at"

    )



    notifications=Notification.objects.filter(

        user=request.user

    ).order_by(

        "-created_at"

    )



    return render(

        request,

        "wallet/wallet.html",

        {

            "wallet":wallet,

            "transactions":transactions,

            "notifications":notifications

        }

    )








# =========================
# WITHDRAW
# =========================


@login_required
def withdraw(request):


    wallet,created=Wallet.objects.get_or_create(

        user=request.user

    )



    if request.method=="POST":


        amount = Decimal(request.POST.get("amount"))

        



        if amount <= float(wallet.balance):



            Withdraw.objects.create(

                user=request.user,

                amount=amount,

                status="PENDING"

            )



            wallet.balance -= amount

            wallet.save()



            WalletTransaction.objects.create(

                user=request.user,

                transaction_type="WITHDRAW",

                amount=amount,

                balance_after=wallet.balance

            )



            Notification.objects.create(

                user=request.user,

                message=f"Withdrawal ₹{amount} requested. Amount will be added between 6 PM to 7 PM."

            )



            messages.success(

                request,

                "Withdraw Request Sent"

            )



            return redirect("withdraw")



        else:


            messages.error(

                request,

                "Insufficient Balance"

            )




    return render(

        request,

        "wallet/withdraw.html",

        {

            "wallet":wallet

        }

    )







# =========================
# ADMIN APPROVE WITHDRAW
# =========================


@login_required
def approve_withdraw(request,id):


    withdraw=get_object_or_404(

        Withdraw,

        id=id

    )


    withdraw.status="Approved"

    withdraw.save()



    Notification.objects.create(

        user=withdraw.user,

        message=f"Withdrawal ₹{withdraw.amount} approved. Amount will reach your bank account."

    )



    return redirect(

        "withdraw_requests"

    )








# =========================
# ADMIN REJECT WITHDRAW
# =========================


@login_required
def reject_withdraw(request,id):


    withdraw=get_object_or_404(

        Withdraw,

        id=id

    )


    withdraw.status="Rejected"

    withdraw.save()



    Notification.objects.create(

        user=withdraw.user,

        message=f"Withdrawal ₹{withdraw.amount} rejected."

    )



    return redirect(

        "withdraw_requests"

    )








# =========================
# WINNING ADD FUNCTION
# =========================


def add_winning_transaction(user, amount):


    wallet,created=Wallet.objects.get_or_create(

        user=user

    )


    wallet.balance += amount

    wallet.save()



    WalletTransaction.objects.create(

        user=user,

        transaction_type="WINNING",

        amount=amount,

        balance_after=wallet.balance

    )



    Notification.objects.create(

        user=user,

        message=f"Congratulations 🎉 You won ₹{amount}. Amount added to wallet."

    )