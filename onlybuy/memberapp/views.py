from django.shortcuts import render,HttpResponse
from .models import *
# Create your views here.

def product_details(request):
    goodid=request.GET["goodid"]
    goods=Goods.objects.get(id=goodid)
    goodsimg=goods.goodsimg_set.all()
    goodsdetail=goods.goodsdetail_set.all()
    goodscolor=goods.

    return HttpResponse()