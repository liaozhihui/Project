import json

from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.core import serializers


# Create your views here.

def request_views(request):
    print(request.scheme)
    print(request.body)
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(request.path)
    print(request.get_full_path())
    print(request.get_host())
    print(request.COOKIES)
    print(request.session)
    print(request.META)
    print(request.META.get("HTTP_REFERER","None"))
    return HttpResponse("查询成功")

def get_views(request):
    if 'uname' in request.GET:
        uname=request.GET['uname']
        print('uname:' + uname)
    if 'uage' in request.GET:
        uage=request.GET['uage']
        print('uage:'+uage)

    return HttpResponse("get请求成功")

def post_views(request):
    if request.method=="GET":
        return render(request,"03-post.html")
    else:
        print(request.POST["uname"])
        print(request.POST['uage'])
        return HttpResponse("注册成功")

def register_views(request):
    if request.method=="GET":
        return render(request,"04-register.html")
    else:
        uname=request.POST.get("uname")
        uage = request.POST.get("uage")
        sex=request.POST.get("sex")
        hobby=request.POST.getlist("hobby")
        jiguan=request.POST.get("jiguan")
        return HttpResponse("注册成功"+str(locals()))

def form_views(request):
    if request.method == "GET":

        form =RemarkForm()
        return render(request,"05-form.html",locals())
    else:
        #1、将request.POST的数据交给RemarkForm()
        form = RemarkForm(request.POST)
        #2、使得form通过验证 - is_valid()
        if form.is_valid():
            #3、获取表单中的值 - cleaned_data
            data=form.cleaned_data
            print(data)
        return HttpResponse("获取数据成功")

def register_exer_views(request):
    if request.method=="GET":
        form=RegisterForm()
        return render(request,"06-register-exer.html",locals())
    else:
        form=RegisterForm(request.POST)
        print(request.POST)
        print(form.errors)
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            user=User()
            user.uname=data['uname']
            user.upwd = data['upwd']
            user.uage = data['uage']
            user.uemail = data['uemail']
            user.save()
        return HttpResponse("注册成功")

def login_views(request):
    if request.method=="GET":
        form = LoginForm()
        return render(request,"07-login.html",locals())

def info_views(request):
    form = InfoForm()
    return render(request,"08-info.html",locals())

def cookie_views(request):
    # if request.method=="GET":
    #     form=CookieForm()
    #     cookie=request.COOKIES
    #     if "uname" in cookie and "upwd" in cookie:
    #         return HttpResponse("欢迎"+cookie["uname"])
    #     return render(request,"09-cookie.html",locals())
    # else:
    #     form=CookieForm(request.POST)
    #     if form.is_valid():
    #         data=form.cleaned_data
    #         user=User.objects.get(uname=data['uname'],upwd=data["upwd"])
    #         resp=HttpResponse("设置成功")
    #
    #         resp.set_cookie("uname",data["uname"],max_age=int(data['alive']))
    #         return resp
    if request.method=="GET":
        #First :check uname and id in cookie
        cookie=request.COOKIES
        if "uname" in cookie and "id" in cookie:

            return HttpResponse("欢迎"+cookie["uname"])
        return render(request,"09-cookie.html")
    else:
        uname=request.POST['uname']
        upwd=request.POST["upwd"]
        duration=request.POST["duration"]
        users=User.objects.filter(uname=uname,upwd=upwd)
        if users:
            resp=HttpResponse("Login OK")
            duration=int(duration)
            max_age=0
            if duration ==1:
                max_age=60*60*24*30
            elif duration==2:
                max_age = 60 * 60 * 24 * 30*6
            elif duration == 3:
                max_age = 60 * 60 * 24 * 365
            resp.set_cookie("id",users[0].id,max_age)
            resp.set_cookie("uname", uname, max_age)
            return resp

        else:
            return HttpResponse("用户名或密码不正确")
        pass


def setsession_views(request):
    request.session['uname'] = 'csdn'
    request.session['upwd'] = '123456'
    return HttpResponse("Set session success")

def getsession_views(request):
    uname=request.session.get("uname","Unkown")
    upwd=request.session.get("upwd","Unkown")
    return HttpResponse("Username:%s,Userpwd:%s"%(uname,upwd))
def server12_views(request):
    name=request.GET["name"]
    age = request.GET["age"]
    return HttpResponse("姓名:%s,年龄:%s"%(name,age))
def json_views(request):
    user={"uname":"lzmaria",
          "age":30,
          "gender":"male",
          "email":"maria@163.com"
          }
    personstr=json.dumps(user)
    return HttpResponse(personstr)

def json_users_views(request):
    users=User.objects.all()
    jsonStr=serializers.serialize("json",users)
    return HttpResponse(jsonStr)


    pass
def server13_views(request):
    uname = request.POST['uname']
    upwd=request.POST['upwd']
    return HttpResponse("注册信息为:%s,%s"%(uname,upwd))

def json_post(request):
    return  render(request,"13-ajax-post.html")
