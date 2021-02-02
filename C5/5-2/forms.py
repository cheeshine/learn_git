# -*- coding:utf-8 -*-
#引入Form基类
from flask_wtf import Form
#引入Form元素父类
from wtforms import StringField,PasswordField
#引入Form验证父类
from wtforms.validators import DataRequired,Length
#登录表单类,继承与Form类
class BaseLogin(Form):
    #用户名
    name=StringField('name',validators=[DataRequired(message="用户名不能为空")
        ,Length(6,16,message='长度位于6~16之间')],render_kw={'placeholder':'输入用户名'})
    #密码
    password=PasswordField('password',validators=[DataRequired(message="密码不能为空")
        ,Length(6,16,message='长度位于6~16之间')],render_kw={'placeholder':'输入密码'})
