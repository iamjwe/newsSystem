from frontend.System import System
from frontend import config


def main():
    System.open(config.host, config.port)
    while System.is_open:
        command = int(input('输入选项:'))
        if command not in range(8):
            print('命令无效')
        else:
            System.menu_resolver(command)


main()
