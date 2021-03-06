"""xuchu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from index import views as index_views
from blog import views as blog_views
from graphene_django.views import GraphQLView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_views.index, name='home'),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('blog_post/<int:id>/', blog_views.blog_post, name='blog_post'),
    path('blog_post_list/', blog_views.blog_post_list, name='blog_post_list'),
]
