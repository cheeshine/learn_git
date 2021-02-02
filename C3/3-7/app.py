#encoding:utf-8
import sys#导入sys模块
from flask import Flask,render_template#导入Flask和render_template模块
app = Flask(__name__)#Flask初始化
@app.route('/')#定义路由
 #视图函数
def hello_world():
     goods = [{'name': '怪味少女开衫外套春秋韩版学生bf原宿宽松运动风2018新款秋装上衣'},
              {'name': 'A7seven 复古百搭牛仔外套女秋季2018新款宽松显瘦休闲夹克衫上衣'},
              {'name': '黑色时尚西装外套女春秋中长款2018新款韩版休闲薄款chic西服上衣'},
              {'name': 'HAVE RICE饭馆 颜值超耐打 复古牛仔外套女短款 2018春秋新款上衣'}
              ]#定义列表goods
     return render_template('index.html',**locals())#渲染模板，并向模板传递值
def do_index_class(index):#定义函数
     if index % 3==0:#每间隔3行输出line
         return 'line'
     else:
         return ''
app.add_template_filter(do_index_class, 'index_class')#使用自定义过滤器添加css
if __name__ == '__main__':
    app.run()




