#encoding:utf-8
from wtforms import Form
from wtforms import StringField, BooleanField # 导入用到的字段
from wtforms.validators import InputRequired, Length, Email # 导入用到的验证器

class LoginForm(Form):
    # email = StringField(
    #     label='邮箱',  # 修改渲染时的value值
    #     validators=[  # 设定字段验证器
    #         InputRequired('邮箱是必填项'),
    #         Email('邮箱格式错误')
    #     ]
    # )
    username= StringField(
        label='用户名',
        validators=[
            InputRequired('用户名为必填项'),
            Length(4, 20, '密码长度为4到20')
        ]
    )
    password = StringField(
        label='密码',
        validators=[
            InputRequired('密码为必填项'),
            Length(6, 9, '密码长度为6到9')
        ]
    )
