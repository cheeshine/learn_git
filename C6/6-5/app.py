from flask import Flask#导入Flask模块
from datetime import datetime#导入datetime模块
import config#导入配置文件
from flask_sqlalchemy import SQLAlchemy#导入SQLAlchemy模块
import pymysql#导入pymysql
pymysql.install_as_MySQLdb()#pymysql替代MySQLdb
app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)# 读取配置参数，将和数据库相关的配置加载到SQLAlchemy对象中
db.init_app(app)#初始化数据库连接文件
#建立表
class Book(db.Model):
    __tablename__='book'#表的别名
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(50),nullable=False)#书名
    publishing_office=db.Column(db.String(100),nullable=False)#出版社
    isbn=db.Column(db.String(100),nullable=False)#isbn号
storage_time=db.Column(db.DateTime,default=datetime.now)#入库时间
db.create_all()  #对象映射
#以上代码同样创建了一个表，下面试着增加一条记录，再增加下面代码：
book1= Book(id='005',title='人工智能导论', publishing_office ='高等教育出版社',isbn='9787040479843')
db.session.add(book1)#把对象添加到会话中
db.session.commit()#提交事务
@app.route('/')
def hello_world():
     return 'Hello World!'
if __name__ == '__main__':
     app.run()

