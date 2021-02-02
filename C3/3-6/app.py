#encoding:utf-8
from flask import Flask,render_template#导入Flask以及render_template模块
app = Flask(__name__)#Flask初始化
@app.route('/')#定义路由
def hello_world():#定义视图函数
     student={#定义字典
         "name":"wangjie",
         "age":-18
     }
     return render_template('index.html',**student)#渲染模板，并向模板传递值
if __name__ == '__main__':
     app.run()



