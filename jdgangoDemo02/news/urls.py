# coding=utf-8
from django.conf.urls import url
from . import views

#进入到urls.py相当与已经匹配到了http://127.0.0.1:8000/index
#地址了，所以在该文件中要继续匹配到剩余的访问路径

urlpatterns = [url(r'^show/$',views.show_views),]