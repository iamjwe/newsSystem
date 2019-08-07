from frontend import Network
from frontend.Menu import get_Menu


class System:
    is_open = False
    Menu = None

    @classmethod
    def open(cls, host, port):
        """打开系统"""
        global socket
        if not cls.is_open:
            cls.is_open = True
            socket = Network.begin_socket(host, port)
            cls.Menu = get_Menu(socket)
        cls.Menu.show_main_menu()

    @classmethod
    def exit(cls):
        """关闭系统"""
        if cls.is_open:
            cls.is_open = False
            Network.end_socket(socket)

    @classmethod
    def menu_resolver(cls, num):
        if num ==1:
            cls.Menu.show_all_news_menu()
        if num == 2:
            cls.Menu.show_browse_menu()
        if num == 3:
            cls.Menu.show_add_menu()
        if num == 4:
            cls.Menu.show_release_menu()
        if num == 5:
            cls.Menu.show_revoke_menu()
        if num == 6:
            cls.Menu.show_delete_menu()
        if num == 7:
            cls.Menu.show_main_menu()
        if num == 0:
            cls.exit()
