import socket
#쓰레드 사용하기 위한거
import threading
#이건 타임묘듈
import time
class SockServer:
    def __init__(self, address, port):
        #바인할 ip port
        self.addr = address
        self.port = port

        #소켓생성
        self.sock = socket.socket()


        #클라이언크 소켓 리스트
        self.clients = []

    def accept(self):
        self.sock.bind(
            (self.addr, self.port)

        )
        self.sock.listen(5)
        while True:
            client_sock, address = self.sock.accept()
            client_sock.settimeout(0.01)
            self.clients.append(client_sock)
            print(address, "에서 연결")
    def send(self):
        while True:
            try:
                msg = input()
                for c in self.clients:
                    c.send(bytes(msg, encoding='utf8'))
            except socket.timeout:
                continue

    #클라이언트 소켓으로 부터 데이서 수신
    def recv(self):
        while True:
            try:
                for c in self.clients:
                    data = c.recv(255)
                    msg = data.decode(encoding='utf8')
                    print(msg)
            except socket.timeout:
                continue
    #통신 시작 함수
    def communicate(self):
        t_accept = threading.Thread(target=self.accept, daemon=True)
        t_send = threading.Thread(target=self.send, daemon=True)
        t_recv = threading.Thread(target=self.recv, daemon=True)

        #쓰레드 시작
        t_accept.start()
        t_send.start()
        t_recv.start()

        #프로그램 종료 방지
        while True:
            time.sleep(1000)


server = SockServer('127.0.0.1', 3000)
server.communicate()
