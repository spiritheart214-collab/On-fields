from django.urls import path, include
from .views import index, send_email



app_name = 'index'

urlpatterns = [
    path("", index, name="index"),
    path("tutorials/", include("tutorials.urls")),
    path("news/", include("news.urls")),
    path("send-email/", send_email, name="send_email"),
]


