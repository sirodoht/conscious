from random import randint

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        return self.username


class Conversation(models.Model):
    title = models.CharField(max_length=200)
    active_statement = models.ForeignKey(
        "Statement",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="active",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    # return a random statement that the user has not voted on yet
    def get_next_available_statement(self, user):
        return Statement.objects.filter(conversation=self).exclude(
            vote__user=user
        ).order_by("?").first()

    def __str__(self):
        return self.title

    def json(self):
        return {
            "title": self.title,
            "created_at": self.created_at,
            "active_statement": self.active_statement
        }


class Statement(models.Model):
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    @property
    def agree_count(self):
        return Vote.objects.filter(
            value=Vote.AGREE,
            statement=self,
        ).count()

    @property
    def disagree_count(self):
        return Vote.objects.filter(
            value=Vote.DISAGREE,
            statement=self,
        ).count()

    @property
    def pass_count(self):
        return Vote.objects.filter(
            value=Vote.PASS,
            statement=self,
        ).count()

    def __str__(self):
        return self.text


class Vote(models.Model):
    AGREE = "agree"
    DISAGREE = "disagree"
    PASS = "pass"
    VALUE_CHOICES = [
        (AGREE, "agree"),
        (DISAGREE, "disagree"),
        (PASS, "pass"),
    ]
    value = models.CharField(max_length=20, choices=VALUE_CHOICES)
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.value} ({self.statement.id}: {self.statement.text[:10]}...)"
