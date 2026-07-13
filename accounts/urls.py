from django.urls import path
from . import views


urlpatterns = [

    path(
        'register/',
        views.register,
        name='register'
    ),


    path(
        'bank-account/',
        views.bank_account,
        name='bank_account'
    ),


    path(
        'login/',
        views.login_view,
        name='login'
    ),


    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

]