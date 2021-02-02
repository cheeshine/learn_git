from flask import Flask#导入Flask模块
app = Flask(__name__)#Flask初始化
@app.route('/')#定义路由
def hello_world():#定义视图函数
       return 'Hello World!'#返回值
def user_login(func):#定义函数user_login
       def inner(*args,**kwargs):#定义内部函数inner
        print('登录操作!')#打印输出
        func(*args,**kwargs)
       return inner#返回inner
@user_login#使用装饰器
def news():#定义函数news()
       print(news.__name__)#打印输出此时的函数名称
       print('这是新闻详情页!')#打印输出
news();
@user_login#使用装饰器
def news_list(*args):#定义函数news_list
      page=args[0]#元祖args[0]赋值给page
      print(news_list.__name__)#打印输出函数名
      print('这是新闻列表页的第'+str(page)+'页！')#打印输出
news_list(5)#调用函数news_list
if __name__ == '__main__': #当模块被直接运行时，代码将被运行，当模块是被导入时，代码不被执行
       app.run()

