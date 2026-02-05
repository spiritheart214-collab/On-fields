from django.urls import path
from .views import tutorials, sub_tutorials, articles_list, article

app_name = 'tutorials'

urlpatterns = [
    path("", tutorials, name="tutorials_list"),
    path('<slug:slug_tutorial>/', sub_tutorials, name='sub_tutorials'),
    path('<slug:slug_tutorial>/<slug:slug_sub_tutorial>/',articles_list, name = "articles-list"),
    path('<slug:slug_tutorial>/<slug:slug_sub_tutorial>/<slug:slug_article>/', article, name='article'),
]
