1.如何创建数据库？

    第一步：新建newsdb数据库，字符集为utf8
    
    第二步：导入sql文件夹下的newsdb.sql文件至数据库中
    

2.如何运行后端？

    第一步：安装pymysql：pip install pymysql

    第二步：复制backend文件夹到任意项目的一级目录下

    第三步：打开config文件夹，设置本地数据库的用户密码

    第四步：运行main_service文件，启动服务器

3.如何运行前端？

    第一步：复制frontend文件夹到任意项目的一级目录下
    
    第二步：打开config文件夹，设置访问的服务器ip和端口（任意访问在同一个局域网的服务器都可以）
    
    第三步：运行main_client文件，启动客户端


注意点：

    此项目为数据库、前端、后端分离项目，可分别部署在不同的电脑中，但要保证各config文件信息正确。
