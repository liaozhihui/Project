"""django01 URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #定义一个访问路径:http://127.0.0.1:8000/01-show
    #交给views.py 中的hsow_views(request)处理
    url(r'^01-show/$',views.show_views),
    #访问路径：http://127.0.0.1:8000/login/
    #在页面中输出：这是登录页面
    url(r'^01-login/$',views.login_views),
    #访问路径:http://127.0.0.1:8000/register
    url(r'^01-register/$',views.register_views),
    #访问路径:http://127.0.0.1:8000/02-url/四位数字
    url(r"^02-url/(\d{4})$",views.url_views),

    #访问路径:http://127.0.0.1:8000/03-url/四位数字/1-2位数字/1-2为数字
    #输出生日
    url(r"^03-url/(\d{4})/(\d{1,2})/(\d{1,2})/$",views.url03_views),
    #访问路径:http://127.0.0.1:8000/04-url/两位及以上的非空白字符/1-2位数字/
    #输出：姓名和年龄
    url(r"^04-url/(\S{2,})/(\d{1,2})/$",views.url04_views),

]
