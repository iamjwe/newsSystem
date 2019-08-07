# 初始化数据库脚本，自动创建数据库结构。遇到delimiter更改结束符就会失败，待解
import pymysql

personal_var_dict = {'user': 'root', 'password': 'root'}  # 请修改成您自己的数据库密码

conn = pymysql.connect(host='127.0.0.1', db='mysql', user=personal_var_dict['user'],
                       password=personal_var_dict['password'], charset='utf8')
cur = conn.cursor()
cur.execute("drop database if exists newsdb")
cur.execute("CREATE DATABASE newsdb CHARACTER SET utf8 COLLATE utf8_general_ci")
cur.execute('use newsdb')
with open(r'.\newsdb.sql', 'r', encoding='utf-8') as f:
    sql_list = f.read().split(';')[:-1]  # 切片获取到所有以;结尾的SQL段
    sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql_list]  # 将每段sql里的换行符改成空格
for sql_item in sql_list:
    cur.execute(sql_item)
conn.commit()
conn.close()
