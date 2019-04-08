# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','category')
 
admin.site.register(Article,ArticleAdmin)
