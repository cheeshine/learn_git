from flask import Flask,request,Response
app = Flask(__name__)
@app.route('/')
def set_cookie():
    # 先创建响应对象
    resp=Response("设置Cookie!")
    #设置cookie名为username,cookie名字为zhangsan,默认关闭浏览器失效
    resp.set_cookie("username", "zhangsan", max_age=7200)
    return resp
@app.route('/get_cookie')
def get_cookie():
    if  request.cookies.get('username'):
        username= request.cookies.get('username')
    else:
        username="Cookie不存在!"
    return username
@app.route("/del_cookie")
def delete_cookie():
    resp = Response("删除Cookie!")
    resp.delete_cookie("username")
    return resp
if __name__ == '__main__':
    app.run(debug=True)
