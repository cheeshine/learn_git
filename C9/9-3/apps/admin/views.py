#encoding:utf-8
from flask import Blueprint,render_template,request,session,redirect,url_for
from .models import Users
bp=Blueprint("admin", __name__,url_prefix='/admin')
@bp.route('/')
def index():
    return "这是后台首页！"