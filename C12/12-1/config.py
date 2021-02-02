#encoding:utf-8
import os
ADMIN_USER_ID = 'JIAQICMSJIQI'
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
WTF_CSRF_ENABLED = False#关闭CSRF保护
#上传到本地
UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'static','images')


