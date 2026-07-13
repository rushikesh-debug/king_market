from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from .models import BankAccount
from django.contrib.auth import logout


User = get_user_model()



# ==========================
# REGISTER
# ==========================

def register(request):

    if request.method == "POST":


        username = request.POST.get(
            "username"
        )


        


        password = request.POST.get(
            "password"
        )



        user = User.objects.create_user(

            username=username,

            

            password=password

        )



        user.save()



        # temporary user id store

        request.session["new_user_id"] = user.id



        return redirect(
            "bank_account"
        )



    return render(

        request,

        "accounts/register.html"

    )









# ==========================
# BANK ACCOUNT
# ==========================


def bank_account(request):


    user_id = request.session.get(
        "new_user_id"
    )



    if not user_id:


        return redirect(
            "register"
        )




    user = User.objects.get(
        id=user_id
    )





    if request.method == "POST":



        BankAccount.objects.create(


            user=user,


            account_holder=request.POST.get(
                "account_holder"
            ),



            bank_name=request.POST.get(
                "bank_name"
            ),



            account_number=request.POST.get(
                "account_number"
            ),



            ifsc=request.POST.get(
                "ifsc"
            )


        )



        # remove session

        del request.session[
            "new_user_id"
        ]



        return redirect(
            "login"
        )





    return render(

        request,

        "accounts/bank_account.html",

        {

            "user":user

        }

    )









# ==========================
# LOGIN
# ==========================


def login_view(request):


    if request.method == "POST":



        username = request.POST.get(
            "username"
        )


        password = request.POST.get(
            "password"
        )




        user = authenticate(

            request,

            username=username,

            password=password

        )




        if user is not None:



            login(

                request,

                user

            )



            return redirect(
                "dashboard"
            )




    return render(

        request,

        "accounts/login.html"

    )
    
    # ==========================
# LOGOUT
# ==========================

def logout_view(request):

    logout(request)

    return redirect("login")