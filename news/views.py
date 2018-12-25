from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Column, Article
# Create your views here.


def index(request):
    columns = Column.objects.all()
    return render(request, 'news/index.html', {'columns': columns})


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})


def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
    if article_slug != article_slug:
        return redirect(article, permanent=True)
    return render(request, 'news/article.html', {'article': article})
