  # -*-coding:utf8-*-
from flask_script import Manager#导入Manager模块
from app import app#导入app
manager = Manager(app)# 创建Manager的实例manager
@manager.option('-n', '--name', dest='name', help='Your name', default='world')#创建命令
@manager.option('-u', '--url', dest='url', default='www.csdn.com')#创建命令
def hello(name, url):#定义函数hello
       'hello world or hello <setting name>'
       print('hello',name)#打印输出
       print(url)#打印输出
if __name__ == '__main__':
       manager.run()