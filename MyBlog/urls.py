"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from blog.views import IndexView, CategoryView, CategoryNameView, ArchivesView, AboutView, SearchView, ArticleView
from blog.feeds import AllArticleRssFeed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path(r'^category/$', CategoryView.as_view(), name='category'),
    path(r'^category/(?P<category_name>.*)/$', CategoryNameView.as_view(), name='category_name'),
    path(r'^archives/$', ArchivesView.as_view(), name='archives'),
    path(r'^about/$', AboutView.as_view(), name='about'),
    path(r'^search/$', SearchView.as_view(), name='search'),
    path(r'^article/(?P<article_title>.*)/$', ArticleView.as_view(), name='article'),
    path(r'^feed/$', AllArticleRssFeed(), name='feed'),
]

# 404 500页面
handler404 = 'blog.views.page_not_found'
handler500 = 'blog.views.server_error'
