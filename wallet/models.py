from django.db import models
from django.conf import settings



# ==================================
# RECHARGE REQUEST
# ==================================

class RechargeRequest(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    utr_number = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )


    status = models.CharField(
        max_length=20,
        default="PENDING"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return f"{self.user.username} - ₹{self.amount}"




# ==================================
# WALLET
# ==================================

class Wallet(models.Model):


    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return f"{self.user.username} - ₹{self.balance}"





# ==================================
# WITHDRAW REQUEST
# ==================================

class Withdraw(models.Model):


    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )


    status = models.CharField(
        max_length=20,
        default="PENDING"
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return f"{self.user.username} - ₹{self.amount}"
    
    from django.db import models
from django.conf import settings



class Notification(models.Model):

    user = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE

    )


    message = models.TextField()



    is_read = models.BooleanField(

        default=False

    )



    created_at = models.DateTimeField(

        auto_now_add=True

    )



    def __str__(self):

        return self.user.username
    
    from django.conf import settings


class WalletTransaction(models.Model):

    TYPE_CHOICES = (

        ("RECHARGE","Recharge"),

        ("BET","Bet"),

        ("WIN","Win"),

        ("WITHDRAW","Withdraw"),

    )


    user = models.ForeignKey(

        settings.AUTH_USER_MODEL,

        on_delete=models.CASCADE

    )


    transaction_type = models.CharField(

        max_length=20,

        choices=TYPE_CHOICES

    )


    amount = models.DecimalField(

        max_digits=10,

        decimal_places=2

    )


    balance_after = models.DecimalField(

        max_digits=10,

        decimal_places=2

    )


    created_at = models.DateTimeField(

        auto_now_add=True

    )


    def __str__(self):

        return self.user.username