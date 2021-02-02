# -*- coding:utf-8 -*-
from flask_script import Manager,Server#导入相应模块
from flask_script import Command#导入Command模块
from app import app#导入app
manager = Manager(app)# 创建Manager的实例manager
@manager.command#使用装饰器
def hello():#定义函数hello()
       'hello world'
       print('hello world')#打印输出
if __name__ == '__main__':
       manager.run()
