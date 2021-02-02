from flask import Flask,flash
from flask import url_for,render_template
# from flask_wtf.csrf import CSRFProtect
#导入定义的BaseLogin
from forms import BaseLogin
import config
app = Flask(__name__)
app.config.from_object(config)
# CSRFProtect(app)
#定义处理函数和路由规则，接收GET和POST请求
@app.route('/login',methods=('POST','GET'))
def baselogin():
    form=BaseLogin()
    #判断是否是验证提交
    if form.validate_on_submit():
        #跳转
        flash(form.name.data+'|'+form.password.data)
        return '表单数据提交成功！'
    else:
        #渲染
        return render_template('login.html',form=form)
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run(debug=True)
