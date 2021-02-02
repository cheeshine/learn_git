# -*- coding: UTF-8 -*-
from flask import Flask
import pymysql #引入mysql库：
pymysql.install_as_MySQLdb()
app = Flask(__name__)
conn = pymysql.Connect(#建立数据库连接
       host='127.0.0.1',
       port=3306,
       user='root',
       passwd='root',
       db='demo_01',
       charset='utf8'
   )
cursor=conn.cursor()# 使用cursor()方法获取操作游标
   #使用try---except进行异常处理
try:
       sql_insert="insert into user(username,email) values ('yanghong1','22222@qq.com')"
       sql_insert1="insert into user(username,email) values ('caoxiao1','33333@qq.com')"
       cursor.execute(sql_insert)
       cursor.execute(sql_insert1)
       conn.commit()
except Exception as e:
       #print e
       print(e)
conn.rollback()
cursor.close()
conn.close()# 关闭数据库连接
@app.route('/')
def hello_world():
       return 'Hello World!'
if __name__ == '__main__':
       app.run()

