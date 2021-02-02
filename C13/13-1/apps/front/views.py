#encoding:utf-8
from flask import Blueprint,render_template,request
bp=Blueprint("front",__name__)#前台访问不需要前缀
@bp.route('/')
def index():
    return  "这是前台首页！"
#注册
@bp.route('/register',methods=['GET','POST'])#定义路由，限制其访问方法
def register():#定义视图函数
    if request.method == 'GET':#如果访问方法为GET方法
        return render_template('front/register.html')#渲染模板
    else:
        pass