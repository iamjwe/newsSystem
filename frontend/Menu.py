from frontend import (Network, config)
import json


def get_Menu(socket):  # 此模块被Waiter模块依赖，不能import Waiter，使用函数来传递数据
    def menu_decorate(need_title, num, char):
        def decorate_menu(f):
            """装饰器方法，用于装饰需要页眉页脚的菜单显示方法"""

            def wrapper(*args, **kwargs):
                Menu.show_header_menu(need_title, num, char)
                f(*args, **kwargs)
                Menu.show_footer_menu(num, char)

            return wrapper

        return decorate_menu

    class Menu:
        """展示菜单"""

        @staticmethod
        def show_header_menu(need_title, num, char):
            """显示公共页眉部分"""
            if need_title:
                print('【新闻发布系统】')
            print(''.center(num, char))

        @staticmethod
        def show_footer_menu(num, char):
            """显示公共页脚部分"""
            print(''.center(num, char))

        @staticmethod
        def show_news(cls, result_lst):
            for i in result_lst:
                id = str(i[0])
                status = '未上线' if i[1] == '0' else '已上线'
                browse_count = str(i[2])
                title = i[3]
                content = i[4]
                cls.show_header_menu(False, 30, '-')
                print(('新闻编号:' + id).ljust(25, ' '), ('标题：' + title).ljust(30, ' '))
                print(('新闻状态:' + status).ljust(25, ' '), ('点击数：' + browse_count).ljust(30, ' '))
                print('新闻内容：' + content)

        @staticmethod
        @menu_decorate(True, 50, '=')
        def show_main_menu():
            """显示主菜单"""
            print('1.查看所有新闻')
            print('2.浏览两条上线新闻')
            print('3.添加未上线新闻')
            print('4.发布未上线新闻')
            print('5.撤销已上线新闻')
            print('6.删除新闻')
            print('7.显示主菜单')
            print('0.退出')

        @staticmethod
        @menu_decorate(False, 30, '*')
        def show_add_menu():
            """显示增加子菜单"""
            title = input('输入新闻标题:')
            content = input('输入新闻内容:')
            res = input('是否要保存输入的数据？<y/n>')
            if res.lower() == 'y':
                Network.request(socket, {'method': 'add_news', 'data': {'title': title, 'content': content}})
                print('添加成功')
            else:
                pass

        @classmethod
        @menu_decorate(False, 30, '*')
        def show_release_menu(cls):
            """显示发布子菜单"""
            result = json.loads(Network.request(socket, {'method': 'get_all_not_release_news', 'data': {}}))
            cls.show_news(cls, result)
            while True:
                id = input('请输入您想发布的新闻编号:')
                Network.request(socket, {'method': 'update_news_to_release', 'data': {'id': id}})
                print('上线成功')
                if input('是否继续发布？<y/n>').lower() != 'y':
                    break

        @classmethod
        @menu_decorate(False, 30, '*')
        def show_revoke_menu(cls):
            result = json.loads(Network.request(socket, {'method': 'get_all_release_news', 'data': {}}))
            cls.show_news(cls, result)
            while True:
                id = input('请输入您想撤销的新闻编号:')
                Network.request(socket, {'method': 'update_news_to_not_release', 'data': {'id': id}})
                print('取消上线成功')
                if input('是否继续撤销？<y/n>').lower() != 'y':
                    break

        @classmethod
        @menu_decorate(False, 30, '*')
        def show_browse_menu(cls):
            """显示浏览子菜单"""
            begin = config.page_begin
            num = config.page_number
            flag = True
            while flag:
                result_str = Network.request(socket,
                                             {'method': 'get_page_news', 'data': {'begin': begin, 'num': num}})
                result = json.loads(result_str)  # 将请求后的结果字符串转为Python对象
                if len(result) == 0:
                    flag = False
                    cls.show_header_menu(False, 30, '-')
                    print('没有更多了')
                    break
                cls.show_news(cls, result)
                if input('是否继续查看两条数据？<y/n>').lower() == 'y':
                    begin = begin + num
                else:
                    # 除大小写y以外的输入全都退出查看
                    break

        @classmethod
        @menu_decorate(False, 30, '*')
        def show_all_news_menu(cls):
            cls.show_news(cls, json.loads(Network.request(socket, {'method': 'get_all_news', 'data': {}})))

        @classmethod
        @menu_decorate(False, 30, '*')
        def show_delete_menu(cls):
            """显示删除子菜单"""
            cls.show_news(cls,json.loads(Network.request(socket,{'method':'get_all_news','data':{}})))
            id = int(input('所有新闻如上，请选择要删除的新闻编号：'))
            res = input('是否要保存输入的数据？<y/n>')
            if res.lower() == 'y':
                Network.request(socket, {'method': 'delete_news', 'data': {'id': id}})
                print('删除成功')

    return Menu
