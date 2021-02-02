#encoding:utf8
from flask_script import Manager #flask 脚本
from flask_migrate import Migrate,MigrateCommand #flask 迁移数据
from app import app,db
from model import User

migrate = Migrate(app,db)#传入2个对象一个是flask的app对象，一个是SQLAlchemy
manager = Manager(app)
manager.add_command('db',MigrateCommand)#给manager添加一个db命令并且传入一个MigrateCommand的类
if __name__=='__main__':
    manager.run()



