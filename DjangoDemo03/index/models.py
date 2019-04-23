from django.db import models

# Create your models here.

#创建一个实体类 - Publisher(表示出版社的信息)
#Django中允许省略自增主键的声明,Django会自动声明
#1、name：出版社名称(字符串)
#2、adress:出版社所在地址(字符串)
#3、city:出版社所在的城市(字符串)
#4、country:出版社所在国家(字符串)
#5、website:网址(字符串)

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country=models.CharField(max_length=30)
    website=models.URLField()
class Author(models.Model):
    name=models.CharField(max_length=12,db_index=True,verbose_name="姓名")
    age=models.IntegerField()
    email=models.EmailField(null=True)
    #增加一个列isActive，表示是否被激活
    isActive=models.BooleanField(default=True)
    def __str__(self):
        return self.name
    #声明内部类-Meta ,定义展现形式
    class Meta:
        #定义表名
        db_table = 'author'
        #定义实体类在admin中的显示名称(单数)

        verbose_name="作者"
        # 定义实体类在admin中的显示名称(复数)
        verbose_name_plural=verbose_name
class Book(models.Model):
    title=models.CharField(max_length=32)
    publicate=models.DateField(null=True)
