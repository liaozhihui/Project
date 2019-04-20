# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/CMS"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DEBUG'] = True
    # 配置自动提交,每次在执行完视图处理函数时将自动提交操作回数据库
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    db.init_app(app)
    from .users import users as users_blueprint

    app.register_blueprint(users_blueprint)
    return app

