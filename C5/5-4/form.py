# -*- coding:utf-8 -*-
from wtforms import Form,FileField,StringField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired,FileAllowed

class UploadForm(Form):
    file = FileField(validators=[FileRequired(),       #FileRequired必须上传
                                   FileAllowed(['jpg','png','gif'])     #FileAllowed:必须为指定的格式的文件
                                   ])
