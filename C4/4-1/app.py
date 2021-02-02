# -*- coding:utf-8 -*-
from flask import Flask,url_for
app = Flask(__name__)
@app.route('/',endpoint='index')
#底层其实是使用add_url_rule实现的
def hello_world():
    return 'Hello World!'
def my_test():
  return '这是测试页面!'
app.add_url_rule(rule='/test/',endpoint='test',view_func=my_test)
with app.test_request_context():
    print(url_for('test'))
if __name__ == '__main__':
    app.run(debug=True)
