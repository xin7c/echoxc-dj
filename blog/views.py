# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def Blog(request):
    post = Article.objects.all()
    print(post)
    return render(request, 'blog.html', {'post': post[0]})
