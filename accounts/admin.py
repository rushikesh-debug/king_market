from django.contrib import admin
from .models import BankAccount


@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):

    list_display = (

        "user",

        "account_holder",

        "bank_name",

        "account_number",

        "ifsc",

        "created_at"

    )