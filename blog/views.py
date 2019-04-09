# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
import logging
# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("default")

# Create your views here.
def blog_post_list(request):
    count = Article.objects.count()
    post_list = Article.objects.values("id","title","content").order_by('id')
    return render(request, 'blog_list.html', {'count': count, 'post_list': post_list})


def blog_post(request, id):
    post = Article.objects.get(id=id)
    REMOTE_ADDR = request.META["REMOTE_ADDR"]
    # print(post)
    logger.debug("来人了")
    collect_logger.info("请求地址:" + REMOTE_ADDR)
    return render(request, 'blog.html', {'post': post})
