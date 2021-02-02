# -*- coding:utf-8 -*-
from functools import wraps
from flask import session,redirect,url_for
import config
#登录限制装饰器
def login_required(func):
     @wraps(func)
     def wrapper(*args, **kwargs):
         if session.get(config.ADMIN_USER_ID):
             return func(*args, **kwargs)
         else:
             return redirect(url_for('admin.login'))
     return wrapper
