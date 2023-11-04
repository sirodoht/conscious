from django.db import models


class Participant:
    pass


class Conversation(models.Model):
    title = models.CharField(max_length=200)
    active_statement = models.ForeignKey(Statement, on_delete=SET_NULL)


class Statement(models.Model):
    text = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_add_now=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)


class Vote(models.Model):
    statement = models.ForeignKey(Statement, on_delete=models.CASCADE)
    value = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_add_now=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
