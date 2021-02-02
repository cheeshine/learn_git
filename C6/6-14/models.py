# -*- coding:utf-8 -*-
from app import db#导入db 对象
class User(db.Model):#定义User类
       __tablename__='user'#表的别名
       id = db.Column(db.Integer,primary_key=True,autoincrement=True)#定义id字段
       username = db.Column(db.String(50),nullable=False)#定义username字段
       password = db.Column(db.String(100),nullable=False)#定义password字段
       telephone = db.Column(db.String(11), nullable=False)#定义telephone字段
