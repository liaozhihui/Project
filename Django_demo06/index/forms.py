# coding=utf-8
from django import forms
from .models import *
#为level控件准备初始化数据
LEVEL_CHOICE=(
    ("1","好评"),
    ("3","差评"),
    ("2","中评"),
)
class RemarkForm(forms.Form):
    #描述一个表示评论内容的表单类
    #控件1-评论标题(title) - 文本框
    title = forms.CharField(label="标题",required=False)
    #控件2-电子邮件(email) - 邮件框
    email = forms.EmailField(label="邮箱",
                             error_messages={"required":"请填写您的邮箱"})
    #控件3-评论内容(message)-多行文本域
    #widget = forms.Textarea 将当前的控件变为多行的文本域
    message = forms.CharField(label="内容",widget=forms.Textarea)
    #控件4-评论级别(level) - 下拉列表
    level = forms.ChoiceField(label="级别",choices=LEVEL_CHOICE)
    #控件5-是否保存(isSaved) - 复选框
    isSaved = forms.BooleanField(label="保存")
    upwd=forms.PasswordInput()

class RegisterForm(forms.ModelForm):
    # upwd = models.CharField(max_length=30)
    # uage = models.IntegerField()
    # uemail = models.CharField(max_length=200)
    # uname=forms.CharField(label="姓名")
    # upwd=forms.CharField(label="密码",widget=forms.PasswordInput())
    # uage=forms.IntegerField(label="年龄")
    # uemail=forms.EmailField(label="邮箱")
    class Meta:
        model=User
        fields=["uname","upwd","uage","uemail"]
        labels={"uname":"姓名","upwd":"密码","uage":"年龄","uemail":"密码"}

class LoginForm(forms.ModelForm):
    class Meta:
        #1、model:指定关联的实体类
        model = User
        #2、fields：指定显示的属性
        fields = ["uname","upwd"]
        #3、labels:指定每个属性对应的label
        labels = {"uname":"登录名称","upwd":"密码"}
        pass
# class InfoForm(forms.Form):
#     uname=forms.CharField(label="用户名称",widget=forms.TextInput(
#         attrs={
#             "placeholder":"请输入用户名",
#             "class":"form-control"
#         }
#     ))
#     upwd = forms.CharField(label="用户密码", widget=forms.PasswordInput(
#         attrs={
#             "placeholder": "请输入用户密码",
#             "class": "form-control"
#         }
#     ))
#     uemail = forms.EmailField(label="用户邮箱", widget=forms.EmailInput(
#         attrs={
#             "placeholder": "请输入邮箱",
#             "class": "form-control",
#         }
#     ))
#     website = forms.CharField(label="个人主站", widget=forms.URLInput(
#         attrs={
#             "placeholder": "请输入网址",
#             "class": "form-control",
#         }
#     ))
#
class InfoForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        labels = {"uname": "姓名", "upwd": "密码", "uage": "年龄", "uemail": "密码"}
        widgets={
            "uname":forms.TextInput(
        attrs={
            "placeholder":"请输入用户名",
            "class":"form-control"
        }),
          "upwd":forms.PasswordInput(
              attrs={
                  "placeholder": "请输入用户密码",
                  "class": "form-control"
              }
          ),
        "uage":forms.NumberInput(
            attrs={
                "placeholder": "请输入用户年龄",
                "class": "form-control"}
        ) ,
        "uemail":forms.EmailInput(
            attrs={
                "placeholder": "请输入邮箱",
                "class": "form-control",
            }
        )


        }


class CookieForm(forms.Form):
    uname=forms.CharField(label='用户名称',widget=forms.TextInput())
    upwd = forms.CharField(label='用户密码', widget=forms.PasswordInput())
    alive=forms.CharField(label="保存时长",widget=forms.TextInput())


