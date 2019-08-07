# 接收服务端发来的欢迎信息
def begin_socket(host,port):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s


def request(socket, json_data):
    import json
    socket.send(json.dumps(json_data).encode('utf-8'))
    return socket.recv(1024).decode('utf-8')


def end_socket(socket):
    socket.send(b'exit')
    socket.close()