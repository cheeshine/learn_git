from flask import Flask,Response
from blue_admin import bp
app = Flask(__name__)
app.register_blueprint(bp)
app.config['SERVER_NAME'] = 'baidu.com:5000'
@app.route('/')
def set_cookie():
      # 先创建响应对象
      resp=Response("设置Cookie!")
      #设置cookie名为username,cookie名字为zhangsan,cookie作用域名
      resp.set_cookie("username", "zhangsan", domain=".baidu.com")
      return resp
if __name__ == '__main__':
    app.run(debug=True)
