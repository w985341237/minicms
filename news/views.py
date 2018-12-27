from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Column, Article
# Create your views here.


def index(request):
    nav_display_columns = Column.objects.filter(nav_display=True)
    home_display_columns = Column.objects.filter(home_display=True)
    return render(request, 'news/index.html', {'nav_display_columns': nav_display_columns,
                                               'home_display_columns': home_display_columns})


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})


def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
    if article_slug != article_slug:
        return redirect(article, permanent=True)
    return render(request, 'news/article.html', {'article': article})
