from flask import Flask
import pymysql
pymysql.install_as_MySQLdb()    #手动指定将MySQLdb转给pymysql处理
app = Flask(__name__)
conn = pymysql.Connect(#配置数据库连接
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='demo_01',
    charset='utf8'
)
cursor = conn.cursor()
sql = "select *from user"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
      username = row[0]
      email= row[1]
     # 打印结果
      print(username)
cursor.close()#关闭游标
conn.close()#关闭连接
@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__ == '__main__':
    app.run()
