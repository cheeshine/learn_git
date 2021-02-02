#delete : 在Memcached中删除指定的一个键值对。
#delete_multi : 在Memcached中删除指定多个键值对。
from flask import Flask
import memcache
app = Flask(__name__)
mc = memcache.Client(['127.0.0.1:11211'],debug=True)#能连接多个服务器
mc.add('key','zhangshan|',time=120)#一次只能设置一个值
key = mc.get('key')#获取数据
print(key)
mc.append('key','wangxiao',time=120)#在第一个键后追加内容
key1=mc.get('key')
print(key1)
mc.delete('key')
print(key)
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run()

