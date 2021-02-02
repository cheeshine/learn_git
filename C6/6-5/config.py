#encoding:utf-8
HOST = '127.0.0.1'
PORT = '3306'
DRIVER='mysqldb'
USERNAME = 'root'
PASSWORD = 'root'
DATABASE = 'db_demo1'
DB_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset-utf8'.format(username=USERNAME,
                                                                                        password=PASSWORD,                                                                      host=HOST,                                                                                port=PORT,                                                                               db=DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
