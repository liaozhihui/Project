# coding=utf-8
from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$',views.index_views),
    url(r'header/$',views.header_views),
    url(r'footer/$',views.footer_views)
]