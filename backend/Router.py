from backend.controller import NewsController


def route_match(method_name,data):
    if method_name == 'add_news':
        return NewsController.add_news(data['title'],data['content'])
    if method_name == 'delete_news':
        return NewsController.delete_news(data['id'])
    if method_name == 'get_page_news':
        return NewsController.get_page_news(data['begin'],data['num'])
    if method_name == 'get_all_news':
        return NewsController.get_all_news()
    if method_name == 'get_all_release_news':
        return NewsController.get_all_release_news()
    if method_name == 'get_all_not_release_news':
        return NewsController.get_all_not_release_news()
    if method_name == 'update_news_to_release':
        return NewsController.update_news_to_release(data['id'])
    if method_name == 'update_news_to_not_release':
        return NewsController.update_news_to_not_release(data['id'])
    if method_name == 'get_news_by_id':
        return NewsController.get_news_by_id(data['id'])
