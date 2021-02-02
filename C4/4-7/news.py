# -*- coding:utf-8 -*-
from flask import Blueprint#导入Blueprint模块
new_list = Blueprint('news', __name__)  # 创建一个blueprint对象。第一个参数可看做该blueprint对象的姓名
# 在一个app里，姓名不能与其余的Blueprint对象姓名重复
# 第二个参数__name__用作初始化
@new_list.route("/news")  # 将蓝图对象当做‘app’那样使用
def new():#定义函数news()
     return '这是新闻模块！'
