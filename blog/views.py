from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import Article, Category, About

import markdown

# Create your views here.


class IndexView(View):
    def get(self, request):
        articles = Article.objects.all().order_by('-create_time')
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(articles, 10, request=request)
        articles = p.page(page)
        return render(request, 'index.html', {
            'articles': articles,
        })


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'categories.html', {
            'categories': categories,
        })


class CategoryNameView(View):
    def get(self, request, category_name):
        category = Category.objects.get(name=category_name)
        return render(request, 'category.html', {
            'category': category,
        })


class ArchivesView(View):
    def get(self, request):
        dates = Article.objects.dates('create_time', 'year', order='DESC')
        archives = {}
        for date in dates:
            archives[date.year] = Article.objects.filter(create_time__year=date.year).order_by('-create_time')
        return render(request, 'archives.html', {
            'archives': archives,
        })


class AboutView(View):
    def get(self, request):
        about = About.objects.all()[0]
        about.about = markdown.markdown(about.about,
                                        extensions=[
                                               'markdown.extensions.extra',
                                               'markdown.extensions.codehilite',
                                               'markdown.extensions.toc',
                                               'markdown.extensions.tables',
                                               ])
        return render(request, 'about.html', {
            'about': about,
        })


class SearchView(View):
    def get(self, request):
        keywords = request.GET.get('keywords', '')
        if keywords:
            articles = Article.objects.filter(
                Q(title__icontains=keywords)|Q(content__icontains=keywords)).order_by('-create_time')
            if articles:
                try:
                    page = request.GET.get('page', 1)
                except PageNotAnInteger:
                    page = 1
                p = Paginator(articles, 10, request=request)
                articles = p.page(page)
                return render(request, 'search.html', {
                    'articles': articles,
                })
            else:
                return render(request, 'search.html', {
                    'msg': '这就触及到我的知识盲区啦！',
                })


class ArticleView(View):
    def get(self, request, article_title):
        article = Article.objects.get(title=article_title)
        article.content = markdown.markdown(article.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                            'markdown.extensions.tables',
                                        ])
        return render(request, 'article.html', {
            'article': article,
        })


def page_not_found(request):
    """
    404
    :param request:
    :return:
    """
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def server_error(request):
    """
    500
    :param request:
    :return:
    """
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response