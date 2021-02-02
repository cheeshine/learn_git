# -*- coding:utf-8 -*-
from flask import Blueprint#导入Blueprint模块
product_list = Blueprint('products', __name__)  # 创建一个blueprint对象。第一个参数可看做该blueprint对象的名字
# 在一个app里，对象名不能与其余的Blueprint对象名重复
# 第二个参数__name__用作初始化
@product_list.route("/products")  # 将蓝图对象当做‘app’那样使用
def product():
       return '这是产品模块！'
