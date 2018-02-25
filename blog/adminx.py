# -*- coding:utf-8 -*- 
__author__ = 'John 2018/2/23 15:16'

import xadmin
from xadmin import views

from .models import Category, Article, About


class GlobalSettings(object):
    site_title = "Pluto's Blog"
    site_footer = "© 2018 Pluto 粤ICP备18018330号"
    menu_style = 'accordion'


class CategoryAdmin(object):
    list_display = ['name', 'create_time']
    search_fields = ['name']
    list_filter = ['name', 'create_time']


class ArticleAdmin(object):
    list_display = ['title', 'category', 'click_nums', 'create_time']
    search_fields = ['title', 'category', 'click_nums']
    list_filter = ['title', 'category', 'click_nums', 'create_time']


class AboutAdmin(object):
    list_display = ['about', 'create_time']
    list_filter = ['about', 'create_time']


xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(About, AboutAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)