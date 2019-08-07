from backend import Router
from backend import config
import socket
import threading
from datetime import datetime
import json


def get_socket():
    serve_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    serve_socket.bind((config.host, config.port))
    serve_socket.listen(5)
    return serve_socket


def log(f):
    """打印来访人员的ip，以及来访时间。"""

    def wrapper(socket, addr):
        f(socket, addr)
        with open('访问日志.txt', 'a', encoding='utf-8') as file:
            file.write(('ip：' + addr[0] + '\t\t' + '时间：' + str(datetime.now()) + '\n'))

    return wrapper


def request_handler(json):
    """处理请求的函数"""
    method_name = json['method']
    data = json['data']
    return Router.route_match(method_name, data)


@log
def personal_thread(client_socket, address):
    """为每一个连接创建一个线程为其服务"""
    while True:
        try:
            data = client_socket.recv(1024)
            if not data or data.decode('utf-8') == 'exit':
                break
            request_data = json.loads(data)  # 将请求数据并转化为json对象
            result_data = request_handler(request_data)  # 处理请求获得结果
            response_json = json.dumps(result_data, ensure_ascii=False)  # 将结果转化为json字符串
            client_socket.send(response_json.encode('utf-8'))
        except ConnectionResetError:
            # 防止前端强制断开连接引发的异常，断开连接就退出循环
            break
    client_socket.close()


def main():
    print('服务器启动')
    serve_socket = get_socket()
    while True:
        # 建立客户端连接
        client_socket, addr = serve_socket.accept()
        # 创建多线程来处理TCP连接
        t = threading.Thread(target=personal_thread, args=(client_socket, addr))
        t.start()


main()
