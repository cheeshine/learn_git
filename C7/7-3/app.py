from flask import Flask
import memcache
app = Flask(__name__)
mc = memcache.Client(['127.0.0.1:11211'],debug=True)#能连接多个服务器
mc.add('key','zhangshan',time=120)#一次只能设置一个值
key = mc.get('key')#获取数据
print(key)
mc.replace('key','lisi',time=120)#一次只能设置一个值
key1=mc.get('key')
print(key1)
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run()
