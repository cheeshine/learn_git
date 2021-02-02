#encoding:utf-8
from exts import db
from datetime import datetime
class Users(db.Model):
    __tablename__='jq_user'
    uid=db.Column(db.Integer,primary_key=True,autoincrement=True)
    #gid=db.Column(db.Integer,nullable=True)
    username=db.Column(db.String(50),nullable=False)#用户名不能为空
    password=db.Column(db.String(100),nullable=False)#密码不能为空
    email=db.Column(db.String(50),nullable=False,unique=True)#用户邮箱不能为空，而且必须是唯一的

