from flask import Flask
import memcache
app = Flask(__name__)
mc = memcache.Client(['127.0.0.1:11211'],debug=True)#能连接多个服务器
mc.add('username','zhangshan',time=0)#一次只能设置一个值
username = mc.get('username')#获取数据
print(username)
# mc.add('username','lisi',time=120)#一次只能设置一个值
# print(username)
dic = {'name': 'to,', 'age': '19', 'job': 'IT'}
mc.set_multi(dic)
mc.replace('username','lisi')
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run()
