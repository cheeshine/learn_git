#encoding:utf-8
from flask import Flask#导入Flask模块
from models import User#导入user模块
from flask_sqlalchemy import SQLAlchemy#导入SQLAlchemy模块
import config#导入配置文件
app = Flask(__name__)#Flask初始化
app.config.from_object(config)#初始化配置文件
db = SQLAlchemy(app)#获取配置参数，将和数据库相关的配置加载到SQLAlchemy对象中
#创建表和字段
db.create_all()#关系映射
@app.route('/')#定义路由
def hello_world():#定义hello_world函数
    return 'Hello World!'
if __name__ == '__main__':
    app.run()
