from flask import Flask#导入Flask模块
app = Flask(__name__) #Flask初始化
@app.route('/')#定义路由
def hello_world():#定义函数
       return 'Hello World!'#返回值
def user_login(func): #定义函数，使用func接收函数作为参数
       def inner():#定义inner()函数
        print('登录操作')#打印输出
        func()#执行func函数
       return inner#返回inner函数，不是返回函数的结果
@user_login#使用了装饰器
def news():#定义函数news
       print('这是新闻详情页')#打印输出
news();#调用news来执行

if __name__ == '__main__':
       app.run()

