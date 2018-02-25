# -*- coding:utf-8 -*- 
__author__ = 'John 2018/2/24 20:44'

from django import template

from blog.models import Article


register = template.Library()


@register.simple_tag
def get_rand_articles(num=3):
    return Article.objects.all().order_by('?')[:num]


@register.simple_tag
def get_articles_count():
    return Article.objects.all().count()