import markdown
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import Article, Category, About


class IndexView(View):
    def get(self, request):
        queryset = Article.objects.all().order_by('-create_time')
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        p = Paginator(queryset, page_size)
        articles = p.get_page(page)
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
        about = About.objects.first()
        if not about:
            return render(request, 'about.html', {
                'about': '后台添加说明',
            })
        about.about = markdown.markdown(about.about,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                            'markdown.extensions.tables',
                                        ])
        return render(request, 'about.html', {
            'about': about.about,
        })


class SearchView(View):
    def get(self, request):
        queryset = Article.objects.all()

        keywords = request.GET.get('keywords', '')
        if keywords:
            queryset = queryset.filter(
                Q(title__icontains=keywords) | Q(content__icontains=keywords)).order_by('-create_time')

        if not queryset.exists():
            return render(request, 'search.html', {
                'msg': '这就触及到我的知识盲区啦！',
            })
        page = request.GET.get('page', 1)
        page_size = request.GET.get('page_size', 10)
        p = Paginator(queryset, page_size)
        articles = p.get_page(page)
        return render(request, 'search.html', {
            'articles': articles,
        })


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, *args, **kwargs)
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
