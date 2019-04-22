from django.shortcuts import render,HttpResponse

# Create your views here.

def parent_index(request):
    uname='吕泽'
    return render(request,'01-parent.html',locals())

def child_index(request):
    return render(request,'02-child.html')

def index_views(request):
    return render(request,'index.html')


def cart_views(request):
    return render(request,'cart.html')

def login_views(request):
    return render(request,'login.html')
