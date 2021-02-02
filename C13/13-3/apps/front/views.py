#encoding:utf-8
from flask import Blueprint,render_template,request,flash,redirect,url_for,session
from .forms import  RegisterForm,LoginForm
from .models import Members
from exts import db
from config import MEMBER_USER_ID
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
#登录
@bp.route('/login',methods=['GET','POST'])#定义路由，限制其访问方法
def login():#定义视图函数
    if request.method == 'GET':#如果访问方法为GET方法
        url = request.args.get('url')#接收网址的参数
        if url=='/log_out':#如果收到的为url内容为/log_out，则处理成'/'
            url='/'
        if url==None:#url为空值的处理
            session['url']=None
        else:
            session['url'] = url#url为非空，直接存到session中
        return render_template('front/login.html')#渲染模板
    else:
        form=LoginForm(request.form)#验证登录表单
        if form.validate():#如果表单验证通过
            username = form.username.data#取得表单username的值放到username中
            password = form.password.data#取得表单的值放到username中
            users = Members.query.filter_by(username=username).first()#按用户名取得用户相关记录
            if users:#如果用户存在
                if username == users.username and users.check_password(password):#验证用户名和校验密码
                    session[MEMBER_USER_ID] = users.username#将username对应的信息存到session中
                    session.permanent = True#实现回话持久化
                    bp.permanent_session_lifetime = timedelta(days=7)#默认保持一周
                else:
                    flash('用户账号或密码错误','error')#如果用户密码不对，则用消息闪现机制予以提示
                    return redirect(url_for('front.login'))#登录失败，网页重新定位到用户登陆页
            else:#用户输入用户错
                flash('用户账号或密码错误', 'error')#如果用户输入用户名错，则用消息闪现机制予以提示
                return redirect(url_for('front.login'))#登录失败，网页重新定位到用户登陆页
        else:
            errors = form.errors#获取表单验证出错信息
            flash(errors,'error')#如果表单验证没有通过，则用消息闪现机制予以提示
            return redirect(url_for('front.login'))#登录失败，网页重新定位到用户登陆页
        username = session.get(MEMBER_USER_ID)#取得用户名
        session['username']=username#将username存入session中
        if session['url']==None:
            return render_template('front/index.html', username=username)#渲染模板
        else:
            return redirect(session['url'])#网页重定位到用户登录之前的页面
#注销登录
@bp.route('/log_out')
def log_out():
    session.pop(MEMBER_USER_ID, None)#清除session
    session.pop('username', None)#清除session
    return redirect(url_for('front.index'))#网页重定向