"""
URL configuration for blogpost project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from datainfo.views import add_user,list_user,update_user,delete_user,delete_comment, add_blog,list_blog,update_blog,delete_blog,add_comment,list_comments
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_user/',add_user,name="add_user"),
    path('list_user/',list_user,name="list_user"),
    path('update_user/',update_user,name="update_user"),
    path('delete_user/',delete_user,name="delete_user"),
    # blog urls
    path('add_blog/',add_blog,name="add_blog"),
    path('list_blog/',list_blog,name="list_blog"),
    path('update_blog/',update_blog,name="update_blog"),
    path('delete_blog/',delete_blog,name="delete_blog"),
    #comments
    path('add_comment/',add_comment,name="add_comment"),
    path('list_comments/',list_comments,name="list_comments"),
    path('delete_comment/',delete_comment,name="delete_comment")
]