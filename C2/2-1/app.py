# 从flask框架中导入Flask类
from flask import Flask
# 传入__name__初始化一个Flask实例
app = Flask(__name__)
#这个路由将根URL映射到了hello_world函数上
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    #指定默认主机为是127.0.0.1，port为8888
    app.run(debug=True,host='0.0.0.0', port=8888)
