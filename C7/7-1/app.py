from flask import Flask
import memcache
app = Flask(__name__)
mc = memcache.Client(['127.0.0.1:11211'],debug=True)#能连接多个服务器
mc.set('name','zhangsan')
mc.set_multi({'key1':'wangyong','key2':'zhangsan'})
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run()
