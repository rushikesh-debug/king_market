from django.contrib import admin

from .models import (
    Game,
    ContestEntry,
    Result
)



@admin.register(Game)
class GameAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "open_time",
        "close_time",
        "is_active",
    )






@admin.register(ContestEntry)
class ContestEntryAdmin(admin.ModelAdmin):

    list_display = (

        "player",
        "game",
        "entry_type",
        "selected_number",
        "amount",
        "payment_status",

    )






@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = (

        "game",

        "open_pana",

        "open_single",

        "close_pana",

        "jodi",

        "close_single",

        "result_date",

    )