1.��ע��������Щģ��ĵ���
from flask import Blueprint,render_template,request,flash,redirect,url_for
from .forms import  RegisterForm
from .models import Members
from exts import db
2.��¼��ַ��
http://127.0.0.1:5000/login