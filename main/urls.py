from django.urls import include, path

from main import views


urlpatterns = [
    path("", views.index, name="index"),
]

urlpatterns += [
    path("api/conversations/<conversation_id>/votes/active/"),
]
