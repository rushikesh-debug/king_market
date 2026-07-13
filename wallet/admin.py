from django.contrib import admin

from .models import RechargeRequest, Wallet


@admin.register(RechargeRequest)
class RechargeRequestAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'amount',
        'utr_number',
        'status',
        'created_at'
    )

    list_filter = (
        'status',
    )


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'balance'
    )