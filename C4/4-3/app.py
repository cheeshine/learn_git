#encoding:utf-8
from flask import Flask,render_template,request,views#导入相应模块
app = Flask(__name__)#Flask初始化
@app.route('/')#定义路由
def hello_world():#定义视图函数
       return render_template('index.html')#渲染模板
class LoginView(views.MethodView):#定义LoginView类
       # 当用户通过get方法进行访问的时候执行get方法
       def get(self):#定义get函数
           return render_template("index.html")#渲染模板
       # 当用户通过post方法进行访问的时候执行post方法
       def post(self):#定义post 函数
           username = request.form.get("username")#接收表单中传递过来的用户名
           password = request.form.get("pwd")#接收表单中传递过来的密码
           if username == 'admin' and password == 'admin':#如果用户名和密码是否为admin
               return "用户名正确，可以登录！"#i f语句为真的话，返回可以登录信息
           else:
               return "用户名或密码错误,不可以登录！"#否则，返回不可以登录信息
   # 通过add_url_rule添加类视图和url的映射关系
app.add_url_rule('/login',view_func=LoginView.as_view('loginview'))
if __name__ == '__main__': #当模块被直接运行时，代码将被运行，当模块是被导入时，代码不被执行
       app.run(debug=True)#开启调试模式

