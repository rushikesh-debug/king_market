from django.db import models
from django.conf import settings



# 🎮 GAME MASTER

class Game(models.Model):

    name = models.CharField(
        max_length=100
    )


    open_time = models.TimeField()


    close_time = models.TimeField()


    is_active = models.BooleanField(
        default=True
    )



    def __str__(self):

        return self.name







# 🎯 USER BET ENTRY

class ContestEntry(models.Model):


    BET_TYPE_CHOICES = (

        ("SINGLE", "Single"),

        ("JODI", "Jodi"),

        ("PANA", "Pana"),

    )



    player = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE

    )



    game = models.ForeignKey(

        Game,

        on_delete=models.CASCADE

    )



    entry_type = models.CharField(

        max_length=20,

        choices=BET_TYPE_CHOICES

    )



    selected_number = models.CharField(

        max_length=10

    )



    amount = models.DecimalField(

        max_digits=10,

        decimal_places=2

    )




    possible_win = models.DecimalField(

        max_digits=10,

        decimal_places=2,

        default=0

    )




    PAYMENT_STATUS = (

        ("PENDING","Pending"),

        ("SUCCESS","Success"),

        ("FAILED","Failed"),

    )



    payment_status = models.CharField(

        max_length=20,

        choices=PAYMENT_STATUS,

        default="SUCCESS"

    )



    utr_number = models.CharField(

        max_length=50,

        blank=True,

        null=True

    )



    created_at = models.DateTimeField(

        auto_now_add=True

    )



    def __str__(self):

        return (

            f"{self.player.username} - "

            f"{self.game.name} - "

            f"{self.selected_number}"

        )









# 🏆 RESULT SYSTEM


class Result(models.Model):


    game = models.ForeignKey(

        Game,

        on_delete=models.CASCADE

    )



    open_pana = models.CharField(

        max_length=3,

        blank=True,

        null=True

    )


    open_single = models.CharField(

        max_length=1,

        blank=True,

        null=True

    )



    close_pana = models.CharField(

        max_length=3,

        blank=True,

        null=True

    )


    close_single = models.CharField(

        max_length=1,

        blank=True,

        null=True

    )



    jodi = models.CharField(

        max_length=2,

        blank=True,

        null=True

    )



    result_date = models.DateField()



    # ⏰ AUTO RESULT PUBLISH TIME

    publish_time = models.TimeField(

        default="11:00"

    )




    created_at = models.DateTimeField(

        auto_now_add=True

    )





    def __str__(self):

        return (

            f"{self.game.name} - "

            f"{self.result_date}"

        )