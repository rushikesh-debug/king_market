# accounts/models.py
from django.contrib.auth.models import AbstractUser

from django.db import models

class User(AbstractUser):
        mobile = models.CharField(max_length=15, null=True, blank=True)
        
class BankAccount(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    account_holder = models.CharField(
        max_length=100
    )

    account_number = models.CharField(
        max_length=50
    )

    ifsc = models.CharField(
        max_length=20
    )

    bank_name = models.CharField(
        max_length=100
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.account_holder