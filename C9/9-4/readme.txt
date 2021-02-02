1.请确保数据库中有jiaqinews这个数据库。
2.请依次执行下面命令：
（1）	执行命令： “python  manager.py db init”，然后回车，进行初始化。
（2）	执行命令： “python  manager.py db migrate”，然后回车，创建迁移脚本。
（3）	执行命令：“ python  manager.py db upgrade”，然后回车，升级数据库。
（4）	执行命令：“ python  manager.py db upgrade”，然后回车。
（5）	执行命令：“python manager.py create_user -u admin -p 123456 -e 472888778@qq.com”。
  如果第（5）步不成功，请检查表中是否有字段password。
3.添加的管理员账号中的邮箱地址不能和已经添加的邮箱地址一样，否则插入数据库会出错!!!!