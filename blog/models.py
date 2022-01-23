from datetime import datetime

from django.db import models


# Create your models here.


class Category(models.Model):
    """
    分类
    """
    name = models.CharField(max_length=10, verbose_name='分类名称')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_articles(self):
        return Article.objects.filter(category=self).order_by('-create_time')


class Article(models.Model):
    """
    文章
    """
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField(verbose_name='正文')
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.SET_NULL, null=True, blank=True,
                                 default=None)
    click_nums = models.IntegerField(default=0, verbose_name='点击量')
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class About(models.Model):
    """
    关于
    """
    about = models.TextField(verbose_name='关于我', null=True, blank=True)
    create_time = models.DateTimeField(default=datetime.now, verbose_name='创建时间')

    class Meta:
        verbose_name = '关于'
        verbose_name_plural = verbose_name
