#append : 修改指定key的值，在该值后面追加内容。
#prepend : 修改指定key的值，在该值前面插入内容。
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
mc.prepend('key','wuyong|',time=120)  #在第一个键前面追加
key2=mc.get('key')
print(key2)
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run()

