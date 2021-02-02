#encoding:utf-8
from flask import Flask,render_template#导入Flask以及render_temlate模块
app = Flask(__name__)#Flask模块初始化
@app.route('/')#定义路由
def hello_world():#定义视图函数
       goods = [{'name': '怪味少女开衫外套春秋韩版学生bf原宿宽松运动风2018新款秋装上衣',  'price': 138.00},
                {'name': 'A7seven 复古百搭牛仔外套女秋季2018新款宽松显瘦休闲夹克衫上衣',  'price': 100.00},
                {'name': '黑色时尚西装外套女春秋中长款2018新款韩版休闲薄款chic西服上衣', 'price': 100.00},
                {'name': 'HAVE RICE饭馆 颜值超耐打 复古牛仔外套女短款 2018春秋新款上衣', 'price': 129.00}
               ]#定义列表goods
       return render_template('shop.html', **locals())#渲染模板，并向模板传递参数
if __name__ == '__main__':#模块可以直接运行
       app.run()


