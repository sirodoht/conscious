from django.urls import include, path

from main import views


urlpatterns = [
    path("", views.index, name="index"),
    path("gate/", views.gate, name="gate"),
    path("vote/<int:statement_id>/<slug:value>/", views.vote, name="vote"),
]

# mobile app API
urlpatterns += [
    path(
        "api/conversations/<slug:conversation_id>/votes/active/",
        views.api_vote,
        name="api_vote",
    ),
]
