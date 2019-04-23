# coding=utf-8
from flask import render_template,request
from ..models import *
from .. import db
from . import products
import json,datetime


@products.route("/goodsinfo")
def goodsinfo():
    return render_template("goodsinfo.html")

@products.route("/queryinfo")
def goodsinfo():
    goodsnum=request.form.get('goodsnum','')
    goodsname=request.form.get('goodsname','')
    starttime=request.form.get('starttime','')
    endtime=request.form.get('endtime','')

    gdict=None

    if starttime and endtime:
        starttime = datetime.datetime.strftime(starttime, "%Y-%m-%d")
        endtime = datetime.datetime.strftime(endtime, "%Y-%m-%d")
        gdict = db.session.query(Product).filter(Product.product_id == goodsnum, \
                                                 Product.product_name == goodsname, \
                                                 Product.create_time > starttime,
                                                 Product.create_time < endtime
                                                 ).all()
    elif starttime:
        starttime = datetime.datetime.strftime(starttime,"%Y-%m-%d")

        gdict=db.session.query(Product).filter(Product.product_id==goodsnum,\
                                     Product.product_name==goodsname,\
                                     Product.create_time>starttime
                                     ).all()
    elif endtime:
        endtime = datetime.datetime.strftime(endtime, "%Y-%m-%d")
        gdict = db.session.query(Product).filter(Product.product_id == goodsnum, \
                                                 Product.product_name == goodsname, \
                                                 Product.create_time < endtime
                                                 ).all()

    strjson=json.dumps(gdict)
    return strjson

@products.route("/alterinfo",methods=["GET","POST"])
def alterinfo():
    if request.method=="GET":
        return render_template("alterinfo.html")
    else:
        product_id=request.form['goodsnum']
        pro=Product.query.fiter_by(product_id=product_id).first()
        pro.prodcut_id=request.form.get("goodsnum")
        pro.product_name=request.form.get("goodsname")
        pro.price=request.form.get("price")
        pro.unit=request.form.get("unit")
        pro.cost_price=request.form.get("costprice")
        pro.category.title=request.form.get("kinds")
        pro.prostock.stock=request.form.get("stock")
        pro.prostock.warning_stock = request.form.get("warningnum")
        pro.proinfo.information = request.form.get("ginfo")
        pro.status=request.form.get("status")


@products.route("/deleteinfo")
def deleteinfo():
    dedict = {}
    goodsnum=request.args.get("product_id")
    good=Product.query.fiter_by(product_id=goodsnum).first()
    dedict['goodsnum']=goodsnum

    dedict['goodsname']=good.product_name
    return render_template("deleteinfo.html",dedict=dedict)

@products.route("/sundeleteinfo")
def subdeleteinfo():

    isnot=request.args.get("isnot")
    goodsnum=request.args.get("goodsnum")
    if isnot:
        pro=Product.query.fiter_by(product_id=goodsnum).first()
        db.session.delete(pro)
    return render_template("isms.html")
