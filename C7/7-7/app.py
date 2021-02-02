from flask import Flask
import memcache
app = Flask(__name__)
mc = memcache.Client(['127.0.0.1:11211'],debug=True)#能连接多个服务器
mc.add('num',99)#一次只能设置一个值
key = mc.get('num')#获取数据
print(key)
mc.incr('num')
key1=mc.get('num')
print(key1)
mc.decr('num',10)
key2=mc.get('num')
print(key2)
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run()
