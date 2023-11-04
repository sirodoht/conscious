from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    def __str__(self):
        return self.username


class Participant(models.Model):
    pass


class Conversation(models.Model):
    title = models.CharField(max_length=200)
    active_statement = models.ForeignKey("Statement", on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Statement(models.Model):
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Vote(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    value = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.value} ({self.statement.id}: {self.statement.text[:10]}...)"

