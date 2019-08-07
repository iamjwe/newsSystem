如何创建数据库？
1.新建newsdb数据库，字符集为utf8
2.导入sql文件夹下的newsdb.sql文件至数据库中

如何运行后端？
0.安装pymysql：pip install pymysql
1.复制backend文件夹到任意项目的一级目录下
2.打开config文件夹，设置本地数据库的用户密码
3.运行main_service文件，启动服务器

如何运行前端？
1.复制frontend文件夹到任意项目的一级目录下
2.打开config文件夹，设置访问的服务器ip和端口（任意访问在同一个局域网的服务器都可以）
3.运行main_client文件，启动客户端


注意点：
此项目为数据库、前端、后端分离项目，可分别部署在不同的电脑中，但要保证各config文件信息正确。
