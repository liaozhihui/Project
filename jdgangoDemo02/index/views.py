from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
# Create your views here.
def index_views(request):
    return HttpResponse("这是index中的url的内容")

def login_views(request):
    return HttpResponse("这是index中的login_views")

def register_views(request):
    return HttpResponse("这是index中的register的用用")

def temp_views(request):
    # t=loader.get_template("01-temp.html")
    # html=t.render()
    # return HttpResponse(html)
    return render(request,"01-temp.html")

def var_views(request):
    # dic={
    #     "uname":"吕泽Maira",
    #     'age':30,
    #     'salary':50000,
    # }
    uname="吕泽Maira"
    age=30
    salary=50000
    print(locals())
    return render(request,'02-var1.html',locals())

def var2_views(request):
    uname = "吕泽Maria"
    age = 30
    salary = 50000
    hobby = ['保健','保健','大保健']
    foods=("大肠刺身","小肠刺身","各种刺身")
    films={'msn':"美少女战士","xmx":"巴拉巴拉小魔仙"}

    animal = Animal()
    animal.name='吕三多'
    t=loader.get_template(
        "03-var2.html"
    )
    html=t.render(locals())
    return HttpResponse(html)


def tag_views(request):
    list = ["潘金莲","李史诗","李白","鲁班七号"]
    return render(request,'04-tag.html',locals())


def static_views(request):
    return render(request,'05-static.html')











class Animal(object):
    name = '旺财'
    def eat(self):
        return self.name+"正在吃饭"