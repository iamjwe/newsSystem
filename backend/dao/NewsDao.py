from backend.dao import connectFactory


def add_news(newsDetail):
    """添加新闻信息的方法"""
    cur = connectFactory.conn.cursor()
    cur.callproc('proc_addnews', (newsDetail.title, newsDetail.content))
    print('请求的方法为：add_news', 'title:' + newsDetail.title, 'content:newsDetail.content')
    connectFactory.conn.commit()


def delete_news(id):
    """删除新闻的方法"""
    cur = connectFactory.conn.cursor()
    cur.callproc('proc_delete_news', (id,))
    print('请求的方法为：delete_news', 'id:' + str(id))
    connectFactory.conn.commit()


def update_news_to_release(id):
    """更新新闻信息的方法"""
    cur = connectFactory.conn.cursor()
    cur.execute(
        "update t_news set is_release='1' where id ={}".format(id))
    print('请求的方法为：update_news_to_release')
    connectFactory.conn.commit()


def update_news_to_not_release(id):
    """更新新闻信息的方法"""
    cur = connectFactory.conn.cursor()
    cur.execute(
        "update t_news set is_release='0' where id={}".format(id))
    print('请求的方法为：update_news_to_not_release')
    connectFactory.conn.commit()


def get_all_news():
    """浏览所有新闻信息的方法"""
    cur = connectFactory.conn.cursor()
    cur.execute(
        'select t1.id,t1.is_release,t1.browse_count,t2.title,t2.content from t_news t1 inner join t_news_detail t2 on t1.newsid=t2.newsid ')
    lst = cur.fetchall()
    print('请求的方法为：get_all_news')
    connectFactory.conn.commit()
    return lst


def get_all_release_news():
    cur = connectFactory.conn.cursor()
    cur.execute(
        "select * from (select t1.id,t1.is_release,t1.browse_count,t2.title,t2.content from t_news t1 inner join t_news_detail t2 on t1.newsid=t2.newsid) as t where is_release='1'")
    lst = cur.fetchall()
    print('请求的方法为：get_all_release_news')
    connectFactory.conn.commit()
    return lst


def get_all_not_release_news():
    cur = connectFactory.conn.cursor()
    cur.execute(
        "select * from (select t1.id,t1.is_release,t1.browse_count,t2.title,t2.content from t_news t1 inner join t_news_detail t2 on t1.newsid=t2.newsid) as t where is_release='0'")
    lst = cur.fetchall()
    print('请求的方法为：get_all_not_release_news')
    connectFactory.conn.commit()
    return lst


def get_page_news(begin, num):
    cur = connectFactory.conn.cursor()
    cur.callproc('proc_page_news', (begin, num))
    lst = cur.fetchall()
    print('请求的方法为：get_page_news', 'begin:' + str(begin) + '   num:' + str(num))
    connectFactory.conn.commit()
    return lst


def get_news_by_id(id):
    """按照新闻编号查询新闻信息的方法"""
    cur = connectFactory.conn.cursor()
    cur.execute(
        "select * from (select t1.id,t1.is_release,t1.browse_count,t2.title,t2.content from t_news t1 inner join t_news_detail t2 on t1.newsid=t2.newsid) as t where id={}".format(id))
    news = cur.fetchone()
    print('请求的方法为：get_news_by_id', 'id:' + str(id))
    connectFactory.conn.commit()
    return news
