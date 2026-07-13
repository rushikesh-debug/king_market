from django.db import models


class AdminBankAccount(models.Model):

    account_holder = models.CharField(
        max_length=100
    )

    bank_name = models.CharField(
        max_length=100
    )

    account_number = models.CharField(
        max_length=50
    )

    ifsc = models.CharField(
        max_length=20
    )

    upi_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )


    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):

        return self.account_holder