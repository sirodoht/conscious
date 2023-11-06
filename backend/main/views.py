from random import randint
from django.contrib import messages
import json
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.http import (
    HttpResponseNotAllowed,
    HttpResponse,
    HttpResponseBadRequest,
    JsonResponse,
)
from django.views.decorators.csrf import csrf_exempt

from main import models


def index(request):
    conversation_list = models.Conversation.objects.all()
    return render(request, "main/index.html", locals())

def get_conversations(request):
    if request.method != "GET":
        return HttpResponseNotAllowed(["GET"])

    conversation_list = models.Conversation.objects.all()
    return JsonResponse(
            {
                "conversations": list(map(lambda x: x.json(), conversation_list))
            }
        )

def vote(request, statement_id, value):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    if value not in ("agree", "disagree", "pass"):
        return HttpResponseBadRequest()
    statement = get_object_or_404(models.Statement, id=statement_id)
    participant = models.Participant.objects.create(
        public_id="a" + str(randint(100, 999))
    )
    vote = models.Vote.objects.create(
        value=value,
        statement=statement,
        participant=participant,
    )
    messages.add_message(request, messages.INFO, "vote registered")
    return redirect("index")


@csrf_exempt
def api_vote(request, conversation_id):
    if request.method != "POST":
        return HttpResponseNotAllowed(["POST"])

    data = json.loads(request.body.decode("utf-8"))

    class VoteForm(forms.Form):
        user_id = forms.CharField()
        vote = forms.CharField()

    form = VoteForm(data)
    if form.is_valid():
        participant_public_id = form.cleaned_data["user_id"]
        vote_value = form.cleaned_data["vote"]
        if vote_value not in ("agree", "disagree", "pass"):
            return JsonResponse(
                {
                    "error": {
                        "vote": ["This field can only be 'agree', 'disagree', 'pass'."]
                    },
                }
            )

        conversation = get_object_or_404(models.Conversation, id=conversation_id)
        statement = models.Statement.objects.filter(conversation=conversation).latest(
            "created_at"
        )
        participant, _ = models.Participant.objects.get_or_create(
            public_id=participant_public_id
        )
        vote = models.Vote.objects.create(
            value=vote_value,
            statement=statement,
            participant=participant,
        )
        return JsonResponse(
            {
                "user_id": participant.public_id,
                "vote": vote.value,
                "registered_at": vote.created_at,
                "error": None,
            }
        )
    else:
        return JsonResponse(
            {
                "error": form.errors,
            }
        )
