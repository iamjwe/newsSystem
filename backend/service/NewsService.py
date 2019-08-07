from backend.dao import NewsDao


def add_news(newsDetail):
    """添加新闻信息的方法"""
    NewsDao.add_news(newsDetail)


def delete_news(id):
    """删除新闻的方法"""
    NewsDao.delete_news(id)


def update_news(id, title=None, content=None):
    """更新新闻信息的方法"""
    print('update_news')


def update_news_to_release(id):
    """更新新闻信息的方法"""
    NewsDao.update_news_to_release(id)


def update_news_to_not_release(id):
    """更新新闻信息的方法"""
    NewsDao.update_news_to_not_release(id)


def get_all_release_news():
    return NewsDao.get_all_release_news()


def get_all_not_release_news():
    return NewsDao.get_all_not_release_news()


def get_all_news():
    """浏览所有新闻信息的方法"""
    return NewsDao.get_all_news()


def get_page_news(begin, num):
    return NewsDao.get_page_news(begin, num)


def get_news_by_id(id):
    """按照新闻编号查询新闻信息的方法"""
    NewsDao.get_news_by_id(id)
