#encoding:utf-8#设定编码
from flask import Flask#导入Flask模块
from models import User#导入User模块
from external import db#导入db模块
import external#导入extenal模块
app = Flask(__name__)#Flask初始化
app.config.from_object(external)#配置文件初始化
db.init_app(app)#初始化数据库连接
#开始创建表和各个字段
with app.app_context():#手动创建应用上下文
    db.create_all()#建立映射
@app.route('/')#定义路由
def hello_world():#定义视图函数
    return 'Hello World!'
if __name__ == '__main__':
    app.run(debug=True)

