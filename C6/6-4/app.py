#encoding:utf8
from flask import Flask#导入Flask模块
from flask_sqlalchemy import SQLAlchemy#导入SQLAlchemy模块
import config#导入配置文件
from datetime import datetime#导入datetime模块
app = Flask(__name__)#Falsk初始化
app.config.from_object(config)#配置文件实例化
#初始化一个数据库连接对象
db=SQLAlchemy(app)
#测试数据库链接是否成功
#建立表
class Book(db.Model):
    __tablename__='book'#表的别名
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)#id号
    title=db.Column(db.String(50),nullable=False)#书名
    publishing_office=db.Column(db.String(100),nullable=False)#出版社
    isbn=db.Column(db.String(100),nullable=False)#isbn号
storage_time=db.Column(db.DateTime,default=datetime.now)#入库时间
db.create_all()#对象映射
@app.route('/')
def index():
   return "index"
if __name__ == '__main__':
    app.run(debug=True)
