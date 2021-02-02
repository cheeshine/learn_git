# -*- coding:utf-8 -*-
from flask import Blueprint, request
bp = Blueprint("admin_bp", __name__, subdomain="admin")
@bp.route("/")
def get_cookie():
    username = request.cookies.get("username")
    # 如果有username这个key，则返回username对应的值，否则返回没有获取到username值
    return username or "没有获取到name值"
