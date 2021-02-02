# -*- coding:utf-8 -*-
from flask import Flask  # 导入Flask模块
import news,products#导入相应模块
app = Flask(__name__)  # 创建 Flask()对象： app
@app.route('/')  # 使用了蓝图，app.route() 这种模式就仍可以使用，注意路由重复的问题
def hello_world():#定义函数
       return 'hello my world !'#返回值
app.register_blueprint(news.new_list)  # 将news模块里的蓝图对象new_list注册到app
app.register_blueprint(products.product_list)  # 将products模块里的蓝图对象product_list注册到app
if __name__ == '__main__':
       app.run(debug=True)  # 调试模式开 启动服务器 运行在默认的5000端口

