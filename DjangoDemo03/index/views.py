from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Sum,Avg,Count,F,Q
from .models import *


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


def create_views(request):
    # 方案1:Entry.objects.create()
    # au1=Author.objects.create(name='老魏',age=40,email="laowei@163.com",isActive=False)
    # print("ID:%s,姓名:%s,年龄:%s,邮箱:%s,激活:%s"%(au1.id,au1.name,au1.age,au1.email,au1.isActive))
    # return HttpResponse("增加数据成功")
    #方案二:obj.save
    # au1=Author(name="蒙蒙")
    # au1.age=18
    # au1.email="mengemng@163.com"
    # au1.save()
    # print("ID:%s,姓名:%s,年龄:%s,邮箱:%s,激活:%s" % (au1.id, au1.name, au1.age, au1.email, au1.isActive))
    # return HttpResponse("增加数据成功")
    # 方案3:obj.save()
    # dic={"name":"WangDB","age":36,"email":"wangdb@163.con","isActive":False}
    # au1 = Author(**dic)
    # au1.save()
    # print("ID:%s,姓名:%s,年龄:%s,邮箱:%s,激活:%s" % (au1.id, au1.name, au1.age, au1.email, au1.isActive))
    #
    # return HttpResponse("增加数据成功")
    obj = Publisher.objects.create(name="清华出版社", adress="北京路", city="北京市", country="China", website="qinghua@163.com")
    return HttpResponse("增加数据成功")
def retrieve_views(request):
    #查看Entry.objects的类型
    # ret=Author.objects
    # print(ret)
    # print(type(ret))
    #2、all()：查询所有数据，并查看返回值
    # authors=Author.objects.all()
    # # print(authors)
    # # print("authors的类型:",type(authors))
    # for au in authors:
    #     print("ID:%s,姓名:%s,年龄:%s,邮箱:%s,激活:%s" % (au.id, au.name, au.age, au.email, au.isActive))
    #3、values():查询返回部分列的信息
    authors=Author.objects.values_list("name","email")
    # for au in authors:
    #     print("姓名:%s,邮箱:%s"%(au['name'],au['email']))
    print(authors)
    return HttpResponse("查询成功")

def filter_views(request):
    # 1、查询id=1的Author的信息
    ret=Author.objects.filter(id=1,name="小泽")
    print(ret)
    authors=Author.objects.filter(name__contains="a")

    for au in authors:
        print("姓名:%s,年龄:%s,邮箱:%s"%(au.name,au.age,au.email))

    return HttpResponse("查询成功")

def filterexer_views(request):
    # 查询年龄在30-40之间的Author的信息
    # 1、查询出age大于等于30的所有的Author
    authors = Author.objects.filter(age__gte=30)
    for au in authors:
        print("姓名:%s,年龄:%s,邮箱:%s" % (au.name, au.age, au.email))
    # 2、查询出所有姓王的Author
    authors = Author.objects.filter(name__startswith="王")
    # 3、查询出Email中包含ao的所有Author
    authors = Author.objects.filter(email__contains="ao")
    # 4、查询出书籍的出版时间在1990 - 2000年之间的图书信息
    books=Book.objects.filter(publicate__year__range=(1990, 2000))

    # 5、查询出Author中年龄大于吕泽Maria年龄的信息
    result=Author.objects.filter(name="WangDB").values("age")
    print(result)
    Author.objects.filter(age__gt=result[0]['age'])
    #5、1合二为一
    Author.objects.filter(age_gt=Author.objects.filter(name='WangDB').values('age'))
    return HttpResponse("查询成功")

def exclude_views(request):
    authors=Author.objects.exclude(id=1)
    for au in authors:
        print("ID:%s,姓名:%s,年龄:%s"%(au.id,au.name,au.age,au.email))

def get_views(request):
    #1、查询id=1 的Author的信息
    author=Author.objects.get(id=1)
    print(author.name)
    #2、查询id>1的Author的信息
    Author.objects.get(id__gt=1)
    return HttpResponse("查询成功")
def aggregate_views(request):
    # result=Author.objects.aggregate(a=Sum('age'),b=Avg('age'))
    # print(result)
    #查询年龄大于30的人的平均年龄和人数
    result=Author.objects.filter(age__gt=30).aggregate(avgAge=Avg("age"),count=Count("*"))
    #查询Author中每个isActive下的人数
    # result=Author.objects.values("isActive").annotate(counter=Count("*"))
    #查询Book 实体中每个时间 所发布额图书数量
    result=Book.objects.values("publicate").annotate(counter=Count("*"))
    print(result)
    for r in result:
        print("组:%s,人数:%s,"%(r["isActive"],r['counter']))
    return HttpResponse("聚合函数查询成功")

def queryall_views(request):
    # authors=Author.objects.filter(isActive=True)
    # authors.update(isActive=True)
    authors=Author.objects.filter(Q(id=1) | Q(age__gt=65))
    print(locals())
    return render(request,"10-queryall.html",locals())

def querybyid_views(request,id):
    print(id)
    author=Author.objects.get(id=id)
    author.age=20
    author.save()
    return render(request,'11-querybyid.html',locals())

def deletebyid_views(request,id):
    try:
        author=Author.objects.get(id=id)
        author.isActive=False
        author.save()
    except Exception as e:
        print(e)
    return redirect("/10-queryall")

def updateall_views(request):
    Author.objects.all().update(age=F('age')+10)
    return redirect("/10-queryall")

def oto_views(request):
    #1、向wife表中增加数据
    #1、1.通过外键属性关联数据
    # wife=Wife()
    # wife.wname="lv夫人"
    # wife.wage=16
    # wife.author_id=1 #关联wife和author
    # wife.save()
    #1.2、通过关联属性关联数据
    # author=Author.objects.get(id=2)
    # wife = Wife()
    # wife.wname="wei夫人"
    # wife.wage=40
    # wife.author=author #关联wife和author
    # wife.save()
    #1.3查询"wei夫人"以及对象的Author的信息
    # wife=Wife.objects.get(wname="wei夫人")
    # print(wife.author)
    # #1.4查询"WangDB"以及对应Wife信息
    # print(Author.objects.get(name="WangeDB").wife.wname)
    book1=Book.objects.get(title="海底两万里")
    book1.publisher_id=2
    book1.save()

    book2=Book.objects.get(title="钢铁是怎样炼成的")

    return HttpResponse("修改成功")

def otm_views(request):
    pub=Publisher.objects.get(name="清华出版社")
    books=pub.book_set.all()
    print(books)

    return HttpResponse("查询数据成功")

def otmexer_views(request,pid):
    #pid表示的是要查看的publisher的id

    #1、查询所有的publisher
    publishers=Publisher.objects.all()
    #根据pid的值来判断查询所有书籍还是按条件查询书籍
    books = Book.objects.all()
    # 2、查询所有的book
    if pid:
        print("pid", pid)
        pid=int(pid)
        if pid >0:
            # books=Book.objects.filter(publisher_id=pid)
            publisher=Publisher.objects.get(id=pid)
            books=publisher.book_set.all()


    print(locals())
    return render(request,"16-otm-exer.html",locals())

def mtm_views(request):
    #将老魏与清华大学出版社关联在一起
    # author = Author.objects.get(name="老魏")
    # publisher=Publisher.objects.get(name__startswith="清华大学出版")
    # author.publishers.add(publisher)
    #1、查询author中id为4的Author所对应的出版社
    author = Author.objects.get(id=4)
    pubs = author.publishers.all()
    print("作者姓名:",author.name)
    print("签约出版社:")
    for pub in pubs:
        print("出版社名称:",pub.name)
    #2、查询publisher中id为1的出版社对应的作者们
    pub=Publisher.objects.get(id=1)
    authors=pub.author_set.all()
    print("出版社名称:",pub.name)
    print("签约作者:")
    for au in authors:
        print("作者姓名:",au.name)
    return HttpResponse("查询数据成功")