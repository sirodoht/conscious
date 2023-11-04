from django.urls import include, path

from main import views


urlpatterns = [
    path("", views.index, name="index"),
]

# mobile app API
urlpatterns += [
#    path("api/conversations/<conversation_id>/votes/active/"),
]
