# -*- coding:utf-8 -*- 
__author__ = 'John 2018/2/26 12:25'

from django.contrib.syndication.views import Feed

from .models import Article


class AllArticleRssFeed(Feed):
    title = "Pluto's Blog"
    link = '/'

    def items(self):
        return Article.objects.all().order_by('-create_time')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return '/article/%s' % item.title