# Queue

class Element:
    # 생성자
    def __init__(self, value, link):
        self.value = value
        self.link = link


class Queue:
    # 생성자
    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, value):
        if self.rear is None and self.front is None:
            elem = Element(value, None)
            self.rear = elem
            self.front = elem
        else:
            elem = Element(value, None)
            self.rear.link = elem
            self.rear = elem

    def dequeue(self):
        if self.front == None:
            return None
        else:
            deq_elem = self.front
            self.front = self.front.link
            return deq_elem.value
        # TODO: 데이터 순서 뒤집기 (이런게 있네)

    def reverse(self):
        c = self.front
        p = None
        while c is not None:
            n = c.link
            c.link = p
            p = c
            c = n
        self.rear, self.front = self.front, self.rear


q = Queue()
for i in range(18):
    q.enqueue(i)
q.reverse()
for i in range(18):
    print(q.dequeue())
