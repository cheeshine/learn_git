from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import config
app = Flask(__name__)
app.config.from_object(config)
db=SQLAlchemy(app)
#定义用户表
class User(db.Model):
    __tablename__ = 'user'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(50),nullable=False)#用户名
    password=db.Column(db.String(50),nullable=False)#密码
    phone=db.Column(db.String(11),nullable=False)#电话
    email=db.Column(db.String(30),nullable=False)#邮箱
    reg_time=db.Column(db.DateTime,default=datetime.now)#注册时间

#定义借书证表
class  Lib_card(db.Model):
    __tablename__='lib_card'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    card_id=db.Column(db.Integer,nullable=False)#借书证id
    papers_type=db.Column(db.String(50),nullable=False)#何种证件办理
    borrow_reg_time=db.Column(db.DateTime,default=datetime.now)#证件办理时间
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    users = db.relationship('User', backref=db.backref('cards'), uselist=False)
db.create_all()
@app.route('/add')
def add():
    #添加两条用户数据
    user1 = User(username="张三", password="111111", phone="13888888888", email="10086@qq.com")
    user2 = User(username="李四", password="123456", phone="13777777777", email="10000@qq.com")
    db.session.add(user1)
    db.session.add(user2)
    #添加两条借书证信息
    card1=Lib_card(card_id='18001', user_id='1', papers_type='身份证')
    card2 =Lib_card(card_id='18002', user_id='2', papers_type='身份证')
    db.session.add(card1)
    db.session.add(card2)
    db.session.commit()
    return '添加数据成功！'
@app.route('/select')
def select():
    user = User.query.filter(User.username == '张三').first()
    art = user.cards
    for k in art:
        print(k)
        print(k.card_id)
    card=Lib_card.query.filter(Lib_card.card_id=='18001').first()
    user=card.users
    print(user.username)
    return "查询数据成功！"

@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run(debug=True)

