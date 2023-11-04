from django.urls import include, path

from main import views


urlpatterns = [
    path("", views.index, name="index"),
]
