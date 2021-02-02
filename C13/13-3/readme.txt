1.请注意下面这些模块的导入
from flask import Blueprint,render_template,request,flash,redirect,url_for
from .forms import  RegisterForm
from .models import Members
from exts import db
2.登录地址：
http://127.0.0.1:5000/login