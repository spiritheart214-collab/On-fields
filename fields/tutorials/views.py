from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Tutorial, Tutorial_subsection, Article

def tutorials(request: HttpRequest):
    context = {
        "tutorials": Tutorial.objects.all(),
    }
    return render(request, "tutorials/tutorials.html", context)

def sub_tutorials(request: HttpRequest, slug_tutorial: str):
    tutorial = get_object_or_404(Tutorial, slug_tutorial=slug_tutorial)
    subsections = tutorial.subsections.all()
    context = {
        "tutorial": tutorial,
        "subsections": subsections,
    }
    return render(request, "tutorials/sub-tutorials.html", context)

def articles_list(request: HttpRequest, slug_tutorial: str, slug_sub_tutorial: str):
    tutorial = get_object_or_404(Tutorial, slug_tutorial=slug_tutorial)
    subsection = Tutorial_subsection.objects.get(slug_sub_tutorial=slug_sub_tutorial)
    context = {
        "tutorial": tutorial,
        "subsection": subsection,
        "articles": subsection.articles.all(),
    }
    return render(request, "tutorials/articles-list.html", context)

def article(request: HttpRequest, slug_tutorial: str, slug_sub_tutorial: str, slug_article:str):
    tutorial = get_object_or_404(Tutorial, slug_tutorial=slug_tutorial)
    subsection = Tutorial_subsection.objects.get(slug_sub_tutorial=slug_sub_tutorial)
    article = Article.objects.get(slug_article=slug_article)
    context = {
        "subsection": subsection,
        "tutorial": tutorial,
        'article': article,
    }
    return render(request, "tutorials/article.html", context)