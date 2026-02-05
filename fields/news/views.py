from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import News_preview, News_article


def news(request: HttpRequest):
    news = News_preview.objects.all()
    context = {
        "news" : news,
    }
    return render(request, 'news/news.html', context)


def news_detail(request: HttpRequest, slug:str):
    article = get_object_or_404(News_article, slug=slug)
    short_title = article.preview.short_title
    context = {
        "article" : article,
        "short_title" :  short_title,
    }
    return render(request, 'news/news-detail.html', context)
