#encoding:utf-8
from flask import Blueprint,render_template,request,flash,redirect,url_for
from .forms import  RegisterForm
from .models import Members
from exts import db
bp=Blueprint("front",__name__)#前台访问不需要前缀
@bp.route('/')
def index():
    return  "这是前台首页！"
#注册
@bp.route('/register',methods=['GET','POST'])#定义路由，限制其访问方法
def register():#定义视图函数
    if request.method == 'GET':#如果访问方法为GET方法
        return render_template('front/register.html')#渲染模板
    if request.method=='POST':#如果访问方法为POST方法
        form = RegisterForm(request.form)#进行表单验证
        username=form.username.data#取得表单username的值放到username中
        password1=form.password1.data#取得表单password1的值放到password1中
        password2=form.password2.data#取得表单password2的值放到password2中
        email=form.email.data#取得表单email的值放到email中
        if password1!=password2:#如果输入的密码不一样
            flash('两次输入的密码不一样', 'error')#用消息闪现予以提示
        else:
            user=Members(username=username,password=password1,email=email
                         )#定义user对象，并对其属性赋值
            db.session.add(user)#插入数据库
            db.session.commit()#提交事务
            flash('注册成功，请登录！','ok')
        return redirect(url_for('front.register'))