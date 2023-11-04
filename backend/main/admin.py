from django.contrib import admin

from main import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "date_joined",
        "last_login",
    )
    list_display_links = ("id", "username")
    search_fields = ("username", "email")


@admin.register(models.Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = (
        "id",
    )


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "active_statement",
    )
    list_display_links = ("id", "title")
    search_fields = ("title", "active_statement")


@admin.register(models.Statement)
class StatementAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "text",
        "conversation",
    )
