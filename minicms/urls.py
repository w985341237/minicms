"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from DjangoUeditor import urls as DjangoUeditor_urls
from news import views
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('ueditor/',include(DjangoUeditor_urls)),
    path('column/<str:column_slug>',views.column_detail,name='column'),
    path('news/<str:article_slug>',views.article_detail,name='article'),
]

# use Django server /media/ files
from django.conf import settings

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)