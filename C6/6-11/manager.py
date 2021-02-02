# -*- coding:utf-8 -*-
from flask_script import Manager,Server#导入相应模块
from flask_script import Command#导入Command模块
from app import app#导入app
manager = Manager(app)# 创建Manager的实例manager
class Hello(Command):#定义Hello类
       'hello world'
       def run(self):#定义函数run
           print('hello world')#打印输出
       # 自定义命令一：
manager.add_command('hello', Hello())#把Hello()子类定义为命令hello
   # 自定义命令二：
manager.add_command("runserver", Server())  # 命令是runserver
if __name__ == '__main__':
       manager.run()
