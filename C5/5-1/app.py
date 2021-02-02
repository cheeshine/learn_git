   #encoding:utf-8#指定编码
from flask import Flask,render_template,request#导入相应模块
app = Flask(__name__)#Flask初始化
@app.route('/')#定义路由
def hello_world():#定义视图函数
     return render_template('index.html')#使用render_template函数渲染模板
@app.route('/login',methods=['GET','POST'])#定义路由，指定访问方法
def login():#定义视图函数
     if request.method=='GET':#如果访问方法为GET方法
         return '这是get请求'#返回应答信息
     else:
         return '这是POST请求'#返回应答信息
if __name__ == '__main__':# 当模块被直接运行时，代码将被运行，当模块是被导入时，代码不被运行。
      app.run(debug=True)#开启调试模式
