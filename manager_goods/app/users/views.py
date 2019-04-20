# coding=utf-8
from flask import render_template,request
from ..models import *
from .. import db
from . import users

@users.route("/")
def index_views():
    return render_template('first.html')

@users.route("/reguser",methods=["GET","POST"])
def reguser():
    if request.method=="GET":
        pass


        return

    else:
        return