# import socket
#
# sock = socket.socket()
#
# sock.connect(
#     ('49.170.237.227', 3000)
#
# )
#
# while True:
#     msg = input("message: ")
#     sock.send(bytes(msg, encoding='utf8'))
#
#     data = sock.recv(255)
#     msg = data.decode(encoding='utf8')
#     print('server', msg)
import socket
import threading
import time
class SockClient:
    def __init__(self, address: str, port: int):
        self.addr = address
        self.port = port
        self.sock = socket.socket()

    def send(self, msg):
        self.sock.send(bytes(msg, encoding='utf8'))


    def recv(self, callback):
        while True:
            data = self.sock.recv(255)
            msg = data.decode(encoding='utf8')
            # 메세지 수신호 콜백함수로 전달
            callback(msg)


    def connect(self):
        self.sock.connect(
            (self.addr, self.port)

        )

# client = SockClient('127.0.0.1', 3000)
# client.communicate()
