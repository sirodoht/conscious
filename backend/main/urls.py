from django.urls import include, path

from main import views


urlpatterns = [
    path("", views.index, name="index"),
    path("gate/", views.gate, name="gate"),
    path("vote/<int:statement_id>/<slug:value>/", views.vote, name="vote"),
    path("conversation/<slug:conversation_id>/", views.conversation, name="conversation"),
]

# API
urlpatterns += [
    path(
        "api/conversations",
        views.get_conversations,
        name="get_conversations"
    ),
    path(
        "api/conversations/<slug:conversation_id>/votes/active/",
        views.api_vote,
        name="api_vote",
    ),
]
