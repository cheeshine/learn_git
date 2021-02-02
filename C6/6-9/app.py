from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config
app = Flask(__name__)
app.config.from_object(config)
db=SQLAlchemy(app)
#定义用户表
#定义模型类-作者类
class Writer(db.Model):
    __tablename__='writer'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
#设置relationship属性方法，建立模型关系，第一个参数为多方模型的类名，添加backref可以实现多对一的反向查询
    books = db.relationship('Book',backref='writers')
#定义模型类-图书类
class Book(db.Model):
    __tablename__='books'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    publishing_office = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(50), nullable=False)
    #设置外键指向一方的主键，建立关联关系
    writer_id= db.Column(db.Integer, db.ForeignKey('writer.id'))
db.create_all()
@app.route('/add')
def add():
    #添加两条作者数据
    user1 = Writer(name="李兴华")
    user2 = Writer(name="Sweigart")
    db.session.add(user1)
    db.session.add(user2)
    #添加两条图书信息
    book1=Book(title='名师讲坛——Java开发实战经典（第2版）', publishing_office='清华大学出版社', isbn='9787302483663',writer_id='1')
    book2 = Book(title='android开发实战', publishing_office='清华大学出版社', isbn='9787302281559',writer_id='1')
    book3 =Book(title='Python游戏编程快速上手', publishing_office='人民邮电大学出版社',isbn='9787115466419',writer_id='2')
    db.session.add(book1)
    db.session.add(book2)
    db.session.add(book3)
    db.session.commit()
    return '添加数据成功！'
@app.route('/select')
def select():
    writer = Writer.query.filter(Writer.id == '1').first()
    book = writer.books
    for k in book:
        print(k)
        print(k.title)
    book=Book.query.filter(Book.id=='1').first()
    writer=book.writers
    print(writer.name)
    return "查询数据成功！"

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
