from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import config
app = Flask(__name__)
app.config.from_object(config)
db=SQLAlchemy(app)

class Book(db.Model):
    __tablename__='book'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    title=db.Column(db.String(50),nullable=False)
    publishing_office=db.Column(db.String(100),nullable=False)
    price=db.Column(db.String(30),nullable=False)
    isbn=db.Column(db.String(50),nullable=False)
    storage_time = db.Column(db.DateTime, default=datetime.now)  # 入库时间
db.create_all()
@app.route('/add')
def add():
    book1=Book(title='Python基础教程（第3版）',publishing_office='人民邮电出版社',price='68.30',isbn='9787115474889')
    book2 = Book(title='Python游戏编程快速上手 第4版', publishing_office='人民邮电出版社', price='54.50', isbn='9787115466419')
    book3 = Book(title='JSP+Servlet+Tomcat应用开发从零开始学', publishing_office='清华大学出版社', price='68.30',isbn='9787302384496')
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.commit()
    return '添加数据成功！'
@app.route('/select')
def select():
    # result=Book.query.filter(Book.id=='1').first()
    result = Book.query.filter(Book.publishing_office == '人民邮电出版社').all()
    for books in result:
        print(books.title,books.publishing_office)
    return "查询数据成功！"
@app.route('/edit')
def edit():
    book1=Book.query.filter(Book.id=='2').first()#查询出id=2的记录
    book1.price=168#修改价格
    db.session.commit()
    return "修改数据成功！"
@app.route('/delete')
def delete():
    book1=Book.query.filter(Book.id=='9').first()
    db.session.delete(book1)
    db.session.commit()
    return '删除数据成功'

@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run(debug=True)
