# coding=utf-8

#HttpResponse 在django中能够向客户端浏览器响应一段文本
from django.http import HttpResponse

def show_views(request):
    '''
    处理业务的视图处理函数
    :param request: 表示的是本次请求的请求对象，封装了请求中所有的信息
    :return: 要响应给客户端的内容
    '''
    return HttpResponse("这是我的第一个Django程序")

def login_views(request):
    '''
    处理业务的视图处理函数
    :param request: 表示的是本次请求的请求对象，封装了请求中所有的信息
    :return: 要响应给客户端的内容
    '''
    return HttpResponse("这是登录界面")

def register_views(request):
    '''
    处理业务的视图处理函数
    :param request: 表示的是本次请求的请求对象，封装了请求中所有的信息
    :return: 要响应给客户端的内容
    '''
    return HttpResponse("这是注册界面")

def url_views(request,year):
    return HttpResponse("传递进来的年份为："+year)

def url03_views(request,year,month,date):
    return HttpResponse("%s年%s月%s日"%(year,month,date))
def url04_views(request,name,age):
    return HttpResponse("姓名:%s，年龄:%s："%(name,age))