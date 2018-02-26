"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import xadmin

from blog.views import IndexView, CategoryView, CategoryNameView, ArchivesView, AboutView, SearchView, ArticleView
from blog.feeds import AllArticleRssFeed


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/$', CategoryView.as_view(), name='category'),
    url(r'^category/(?P<category_name>.*)/$', CategoryNameView.as_view(), name='category_name'),
    url(r'^archives/$', ArchivesView.as_view(), name='archives'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^article/(?P<article_title>.*)/$', ArticleView.as_view(), name='article'),
    url(r'^feed/$', AllArticleRssFeed(), name='feed'),
]
