from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('欢迎来到我的主页！')

def column_detail(request,column_slug):
    return HttpResponse('column_slug:' + column_slug)

def article_detail(request,article_slug):
    return HttpResponse('article_slug:' + article_slug)