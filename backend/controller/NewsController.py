from backend.service import NewsService
from backend.bean.News import NewsDetail


def add_news(title, content):
    """添加新闻信息的方法"""
    news_detail = NewsDetail(title=title, content=content)
    NewsService.add_news(news_detail)
    return {'title': title, 'content': content}


def delete_news(id):
    """删除新闻的方法"""
    NewsService.delete_news(id)


def update_news(id, title=None, content=None):
    """更新新闻信息的方法"""
    print('update_news')


def get_page_news(begin, num):
    return NewsService.get_page_news(begin, num)


def get_all_news():
    """浏览所有新闻信息的方法"""
    return NewsService.get_all_news()


def update_news_to_release(id):
    """更新新闻信息的方法"""
    NewsService.update_news_to_release(int(id))


def update_news_to_not_release(id):
    """更新新闻信息的方法"""
    NewsService.update_news_to_not_release(int(id))


def get_all_release_news():
    return NewsService.get_all_release_news()


def get_all_not_release_news():
    return NewsService.get_all_not_release_news()


def get_news_by_id(id):
    """按照新闻编号查询新闻信息的方法"""
    NewsService.get_news_by_id(id)
