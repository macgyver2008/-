from tkinter import *
from tkinter.ttk import *
from client import *
import threading

class Chat:
    def __init__(self):
        #클라이언트 소켓 생성
        self.client = SockClient(None, None)
        # receive쓰레드
        self.t_recv = None

        # UI생성
        #매인창 생성
        self.root = Tk()
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        # 주소입력란 생성
        # 1. UI 배치를 위한 프레임
        self.frame1 = Frame(self.root)
        self.frame1.pack(side="top", padx=5, pady=5, fill='x')
        # 2. 서버주소 입력창 생성
        self.address_box = Entry(self.frame1)
        self.address_box.pack(side="left", expand=True, fill="both")
        # 3. 서버연결 버튼 생성
        self.connect_btn = Button(self.frame1, text="연결")
        self.connect_btn.pack(side="right", padx=5, fill="both")



        #챗박스 생성
        # 1.UI를위한 프레임
        self.frame2 = Frame(self.root)
        self.frame2.pack(side="top",padx=5,expand=True,fill="both")
        # 2. 스크롤바
        self.scroll = Scrollbar(self.frame2)
        self.scroll.pack(side="right", fill="y")
        # 3 텍스트 리스트 생성
        self.chat_box = Listbox(self.frame2, yscrollcommand=self.scroll.set)
        self.chat_box.pack(side="left", expand=True, fill="both")
        self.scroll.configure(command=self.chat_box.yview)



        self.frame3 = Frame(self.root)
        self.frame3.pack(side="bottom",padx=5,pady=5,fill="x")
        # 이름 입력창 생성
        self.name_box = Entry(self.frame3, state=DISABLED, width=10)
        self.name_box.pack(side="left",fill="both")
        # 3.내용 입력창
        self.input_box = Entry(self.frame3, state=DISABLED)
        self.input_box.pack(side="left",padx=5,expand=True,fill="both")
        #4. 전송버튼
        self.send_btn = Button(self.frame3, text='전송', state=DISABLED)
        self.send_btn.pack(side="right", fill="both")
        # UI끝

        self.connect_btn.configure(command=self.cmd_connect)
        self.send_btn.configure(command=self.cmd_send)
        self.input_box.bind("<Return>", lambda x: self.cmd_send())


        self.root.mainloop()


    def callback_recv(self, msg):
        if type(msg) == str:
            scrollPos = self.chat_box.yview()[1]

            self.chat_box.insert(END, msg)

            if scrollPos == 1.0:
                    self.chat_box.yview_moveto(1.0)



    #연결 커맨드
    def cmd_connect(self):
        try:
            addr_str = self.address_box.get()
            ip, port = addr_str.split(":")
            # 소켓클라이언트의 연결 정보 수정
            self.client.addr = ip
            self.client.port = int(port)

            self.client.connect()

            self.t_recv = threading.Thread(target=self.client.recv, args=(self.callback_recv,))
            self.t_recv.start()
        except Exception:
            #연결 실패시 무시
            pass
        else:
            #예외가 없이 연결레 성공할시
            self.address_box.configure(state=DISABLED)
            self.connect_btn.configure(state=DISABLED)
            self.name_box.configure(state="enabled")
            self.input_box.configure(state="enabled")
            self.send_btn.configure(state="enabled")
    #전송 커맨드
    def cmd_send(self):
        try:
            #이름과 메시지를 입력창으로부터 읽음
            name = self.name_box.get()
            msg = self.input_box.get()
            if len(name) == 0:
                name = 'anonymous'
            if len(msg) == 0:
                return
            self.client.send(name + ': ' + msg)
        except Exception:
            pass
        else:
            self.input_box.delete(0, END)



Chat()
