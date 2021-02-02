1.使用“view-source:http://127.0.0.1:5000/login”进行查看，
然后使用“http://127.0.0.1:5000/login”进行访问，测试登录功能。
2.使用“http://127.0.0.1:5000/register”测试注册功能，查看注册是否能够成功，应该不会成功，因为register页面没有设置csrf_token。