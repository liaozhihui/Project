# coding=utf-8
from django.conf.urls import url
from . import views
urlpatterns=[
            url(r'^01-parent/$',views.parent_index),
            url(r'^02-child/$',views.child_index),
url(r'^cart/$',views.cart_views),
url(r'^index/$',views.index_views),
url(r'^login/$',views.login_views),
url(r'^03-create/$',views.create_views),
url(r'^04-retrieve/$',views.retrieve_views),
url(r'^05-filter/$',views.filter_views),
url(r'^05-filterexer/$',views.filterexer_views),
url(r'^07-exclude/$',views.exclude_views),
url(r'^08-get/$',views.get_views),
url(r'^09-aggregate/$',views.aggregate_views),
url(r'^10-queryall/$',views.queryall_views),
url(r'^11-querybyid/(\d+)$',views.querybyid_views),
url(r'^12-deletebyid/(\d+)$',views.deletebyid_views),
url(r'^13-updateall/$',views.updateall_views),
]
urlpatterns+=[url(r'^14-oto/$',views.oto_views),
              url(r'^15-otm/$',views.otm_views),
              url(r'^16-otm-exer/(\d*)$', views.otmexer_views),
              url(r'^17-mtm/$', views.mtm_views),
              ]