#encoding:utf-8
from flask import Blueprint,render_template,request,session,redirect,url_for,make_response
from .models import Users
from .forms import LoginForm
from utils.captcha import create_validate_code
from io import BytesIO
from datetime import timedelta
bp=Blueprint("admin", __name__,url_prefix='/admin')
@bp.route("/login/",methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        return  render_template('admin/login.html')
    else:
        form=LoginForm(request.form)
        if form.validate():
                user = request.form.get('username')
                pwd = request.form.get('password')
                online = request.form.get('online')
                captcha=request.form.get('captcha')
                if session.get('image').lower() != captcha.lower():
                    return render_template('admin/login.html', message="验证码不对！")
                else:
                        users=Users.query.filter_by(username=user).first()
                        if users:
                                    if user == users.username and users.check_password(pwd):
                                        session['user_id'] = users.uid#用户id存于session
                                        #print(session['user_id'])
                                        # print("密码对！")
                                        if online:  # 如果选择了记住我
                                            session.permanent = True
                                            bp.permanent_session_lifetime = timedelta(days=10)
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
def index():
    return render_template('admin/index.html')
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