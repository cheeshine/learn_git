#encoding:utf8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config#导入配置文件
app = Flask(__name__)
app.config.from_object(config)#配置文件实例化
#初始化一个对象
db=SQLAlchemy(app)
#测试数据库链接是否成功
db.create_all()
@app.route('/')
def index():
   return "index"
if __name__ == '__main__':
    app.run(debug=True)
