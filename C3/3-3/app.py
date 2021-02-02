#encoding:utf-8
from flask import Flask,render_template#导入Flask以及render_template 模块
import random#导入random模块
app = Flask(__name__)#Flask初始化
@app.route('/') #定义路由
def hello_world():#定义视图函数
       rand1=random.randint(0,1)# 产生0-1范围内的整型数
       return render_template('index.html',name=rand1)#渲染模板，并向模板传递值
if __name__ == '__main__': #当模块被直接运行时，代码将被运行，当模块是被导入时，代码不被执行
       app.run(debug=True)#开启调试模式

