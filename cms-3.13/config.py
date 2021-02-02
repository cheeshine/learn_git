#encoding:utf-8
import os
ADMIN_USER_ID = 'JIAQICMSJIQI'
MEMBER_USER_ID='MEMBERREGISTER'
SECRET_KEY = os.urandom(24)
DEBUG=True
DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'jiaqicms'
DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO= False
#上传到本地
UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'static','images')
FLASKY_DB_QUERY_TIMEOUT=0.00005#数据库查询时间的门限值
SQLALCHEMY_RECORD_QUERIES=True
WTF_CSRF_ENABLED = True#关闭或打开Flask csrf保护
#app.config['JSON_AS_ASCII'] = False#Flask 让jsonify返回的json串支持中文显示  修改的
JSON_AS_ASCII=False
