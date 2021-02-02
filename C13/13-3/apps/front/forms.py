#encoding:utf-8
from wtforms import Form
from wtforms import StringField, BooleanField,SubmitField # 导入用到的字段
from wtforms.validators import InputRequired, Length, Email,DataRequired # 导入用到的验证器

class RegisterForm(Form):
    username= StringField(
        label='用户名',
        validators=[
            InputRequired('用户名为必填项'),
            Length(6, 15, '密码长度为4到20')
        ]
    )
    password1 = StringField(
        label='密码',
        validators=[
            InputRequired('密码为必填项'),
            Length(6, 30, '密码长度为6到9')
        ]
    )
    password2 = StringField(
        label='密码',
        validators=[
            InputRequired('密码为必填项'),
            Length(6, 30, '密码长度为6到9')
        ]
    )
    email = StringField(validators=[Length(0, 100, message='邮箱为1-100位')])
class LoginForm(Form):
    username = StringField(
        label='用户名',
        validators=[
            InputRequired('用户名为必填项'),
            Length(6, 15, '密码长度为6到20')
        ]
    )
    password = StringField(
        label='密码',
        validators=[
            InputRequired('密码为必填项'),
            Length(6, 30, '密码长度为6到9')
        ]
    )