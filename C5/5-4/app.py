from flask import Flask,render_template,request,send_from_directory
import time
import os
from os import path
from werkzeug.utils import secure_filename
import platform
from form import UploadForm
from werkzeug.datastructures import CombinedMultiDict
app = Flask(__name__)
if platform.system() == "Windows":
    slash = '\\'
else:
    platform.system()=="Linux"
    slash = '/'
# UPLOAD_PATH = os.path.curdir + os.path.sep + 'uploads' + os.path.sep
UPLOAD_PATH = os.path.curdir + slash + 'uploads' + slash
@app.route('/',methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
       return render_template('upload.html')
    else:
        if not os.path.exists(UPLOAD_PATH):
            os.makedirs(UPLOAD_PATH)#没有目录则创建目录
        form = UploadForm(CombinedMultiDict([request.form, request.files]))
        if form.validate():
             f = request.files['file']
             filename = secure_filename(f.filename)#取得文件名字
             ext = filename.rsplit('.', 1)[1]  # 获取文件后缀
             unix_time = int(time.time())
             new_filename = str(unix_time) + '.' + ext  # 对文件进行重新命名
             file_url=UPLOAD_PATH+new_filename
             print(new_filename)
             print(UPLOAD_PATH)
             print(file_url)
             f.save(path.join(UPLOAD_PATH, new_filename))
             return "上传文件成功！！"
        else:
            return "只支持jpg、png以及gif格式的文件！"
#访问上传的文件
#浏览器访问：http://127.0.0.1:5000/images/xxx.jpg/  就可以查看文件了
@app.route('/images/<filename>/',methods=['GET','POST'])
def get_image(filename):
    dirpath = os.path.join(app.root_path, 'uploads')#得到绝对路径，比如J:\python project\例5-3-2\uploads
    print(dirpath)
    print(filename)
    #return send_from_directory(dirpath,filename,as_attachment=True)#为下载方式
    return send_from_directory(dirpath,filename)#为在线浏览方式
if __name__ == '__main__':
    app.run(debug=True)
