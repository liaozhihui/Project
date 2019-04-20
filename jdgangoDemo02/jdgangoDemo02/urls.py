"""jdgangoDemo02 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #判断进入到服务器之后的访问地址是以 news/作为开始的
    url(r'^news/',include('news.urls')),
    url(r'^music/',include('music.urls')),
url(r'^sport/',include('sport.urls')),
url(r'^index/',include('index.urls')),
    #访问路径不是/admin,/news,/music的时候，交给index的时候，交给index应用中的urls.py去处理
url(r'^',include('index.urls')),
]
