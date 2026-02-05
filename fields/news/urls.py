from django.urls import path
from .views import news, news_detail


app_name = 'news'

urlpatterns = [
    path("", news, name="news-list"),
    path("<slug:slug>", news_detail, name="news-detail"),
]