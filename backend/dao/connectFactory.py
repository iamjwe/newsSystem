from backend import config
import pymysql
conn = pymysql.connect(host=config.host, db='newsdb', user=config.user,
                       password=config.password, charset='utf8')
