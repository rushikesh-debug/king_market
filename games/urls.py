from django.urls import path
from .views import game_play, payment_page

urlpatterns = [

    path(
        'play/<int:game_id>/',
        game_play,
        name='game_play'
    ),

    path(
        'payment/<int:entry_id>/',
        payment_page,
        name='payment_page'
    ),

]