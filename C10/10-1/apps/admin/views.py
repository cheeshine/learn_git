#encoding:utf-8
from flask import Blueprint,render_template,request,session,redirect,url_for,make_response,jsonify,json
from .models import Users,Articles_Cat,Articles_Tag,Articles
from .forms import LoginForm,Article_cat,Article
from utils.captcha import create_validate_code
from io import BytesIO
from datetime import timedelta
from .decorators import login_required
from exts import db
from xpinyin import Pinyin
from sqlalchemy import func#统计查询使用
from sqlalchemy import and_#多个添加查询
import config
import os
import re
import memcache
bp=Blueprint("admin", __name__,url_prefix='/admin')
@bp.route("/login/",methods=['GET', 'POST'])
def login():
    error = None
    # print(session.get('user_id'))
    if request.method == 'GET':
        return  render_template('admin/login.html')
    else:
        form=LoginForm(request.form)
        if form.validate():
                user = request.form.get('username')
                pwd = request.form.get('password')
                online=request.form.get('online')
                captcha=request.form.get('captcha')
                if session.get('image').lower() != captcha.lower():
                    return render_template('admin/login.html', message="验证码不对！")
                else:
                        users=Users.query.filter_by(username=user).first()
                        if users:
                                    # if user == users.username and users.check_password(pwd):
                                    if user == users.username:
                                        #session['user_id'] = users.uid#用户id存于session
                                        session[config.ADMIN_USER_ID] = users.uid
                                        if online:#如果选择了记住我
                                            session.permanent = True
                                            bp.permanent_session_lifetime = timedelta(days=10)
                                            #bp.permanent_session_lifetime = timedelta(minutes=10)
                                            print("设置了session的过期时间！")
                                            print(session.get(config.ADMIN_USER_ID))
                                            #print(session['user_id'])
                                        print("密码对！")
                                        return redirect(url_for('admin.index'))
                                    else:
                                        #print("用户名或密码错！")
                                        error="用户名或密码错！"
                                        return render_template('admin/login.html', message=error)
                        else:
                            return render_template('admin/login.html', message="别试了，没有此用户！")
        else:
               return render_template('admin/login.html', message=form.errors)
@bp.route('/')
@login_required
def index():
    return render_template('admin/index_new.html')
#调用验证码
@bp.route('/code/')
def get_code():
    # 把strs发给前端,或者在后台使用session保存
    code_img, strs = create_validate_code()
    buf=BytesIO()
    code_img.save(buf, 'JPEG', quality=70)
    buf_str = buf.getvalue()
    # buf.seek(0)
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/jpeg'
    # 将验证码字符串储存在session中
    session['image'] = strs
    return response
@bp.route('/test/')
@login_required
def test():
    return 'test index'
@bp.route('/logout/')
@login_required
def logout():
    # del session[config.ADMIN_USER_ID]
    session.pop(config.ADMIN_USER_ID, None)
    return redirect(url_for('admin.login'))
#登录页视图
@bp.route('/welcome/')
@login_required
def welcome():
    return  render_template('admin/welcome.html')
#个人信息页视图
@bp.route('/profile/')
@login_required
def profile():
    #根据session取得用户信息
    if config.ADMIN_USER_ID  in session:
        user_id = session.get(config.ADMIN_USER_ID)
        user = Users.query.get(user_id)

    return render_template('admin/profile.html',user=user)
