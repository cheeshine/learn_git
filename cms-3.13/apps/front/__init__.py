#encoding:utf-8
from .views import bp
from flask import render_template
#404页面
@bp.errorhandler(404)
def miss(e):
    return render_template('front/404.html'), 404