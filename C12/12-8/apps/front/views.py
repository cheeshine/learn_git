#encoding:utf-8
from flask import Blueprint
bp=Blueprint("front",__name__)#前台访问不需要前缀
@bp.route('/')
def index():
    return  "这是前台首页！"