# coding=utf-8
from django.conf.urls import url
from . import views
urlpatterns=[
            url(r'^01-parent/$',views.parent_index),
            url(r'^02-child/$',views.child_index),
url(r'^cart/$',views.cart_views),
url(r'^index/$',views.index_views),
url(r'^login/$',views.login_views),

             ]
