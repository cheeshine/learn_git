from flask import Flask,render_template,request
import os
from werkzeug.utils import secure_filename
app = Flask(__name__)
@app.route('/',methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
       return render_template('upload.html')
    else:
        f = request.files['file']
        basepath = os.path.join(os.path.dirname(__file__),'uploads')  # 当前文件所在路径
        # upload_path = os.path.join(basepath,,secure_filename(f.filename))
        f.save(basepath,secure_filename(f.filename))
        return "上传文件成功！！"
if __name__ == '__main__':
    app.run(debug=True)
