from django.contrib import admin
from .models import *
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    #1、定义在列表页上要显示的字段们
    #属性:list_display
    #取值：由属性名称或列表
    list_display = ("name","age",'email')
    #2、定义在列表页上能够连接到详情页的字段们
    #属性：list_display_links
    #取值：由属性名称组成的元祖或列表
    #注意：取值必须出现在list_display中
    list_display_links = ("name",'email')
    #3、定义在列表页中允许被编辑的字段们
    #属性：list_editable
    #取值：由属性名称组成的元祖或列表
    #注意：取值必须出现在list_display中但不能出现在list_display_links中
    list_editable = ('age',)
    #4、定义在列表页的右侧增加过滤器实现快速筛选
    #属性：list_filter
    #取值：由属性名称组成的元组或列表
    list_filter = ('isActive',)
    #5、添加搜索字段
    #属性：search_fields
    #取值：有属性名称组成的元祖或列表
    search_fields = ("name","email")
    #7、在详情页中，指定要显示的字段以及显示的顺序
    #属性：fields
    #取值：由属性名组成的元祖或列表，元祖或列表中的顺序决定了详情页中显示顺序
    # fields = ("name",'email','age')
    #8、在详情页中对字段进行分组
    #属性：fieldsets
    #注意：fields和fieldsets是不能共存的
    # fieldsets = (
    #     #分组1-包含name和age两个列
    #     ("基本选项",{"fields":('name','age')}),
    #     #分组2-包含email和isActive两个列
    #     ("高级选项",{"fields":("email","isActive"),"classes":("collapse",)})
    # )
    pass
class BookAdmin(admin.ModelAdmin):
    list_display = ("title","publicate")
    #6、指定日期分层选择器
    #属性:date_hierarchy
    #取值：必须为DateFiled或DateTimeField
    date_hierarchy = "publicate"
    pass
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name","adress","city")
    list_editable = ("adress",'city')
    list_filter = ("city","country")
    search_fields = ("name","website")
    # fieldsets = (("基本选项",{"fields":("name","adress","city"),}),
    #              ("高级选项",{"fields":("country","website"),"classes":("collapse",)}))

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Wife)
