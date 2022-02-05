# TODO: DEque
class DEqueElement:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class DEque:
    def __init__(self):
        self.rear = None
        self.front = None

    def insert_rear(self, value):
        V = DEqueElement(value, None, self.rear)
        if self.rear is None:
            self.rear = V
            self.front = V
        else:
            self.rear.left = V
            self.rear = V

    def insert_front(self, value):
        V = DEqueElement(value, self.front, None)
        if self.front is None:
            self.front = V
            self.rear = V
        else:
            self.front.right = V
            self.front = V

    def del_front(self):
        if self.rear is None:
            return None
        value = self.front.value
        if self.rear == self.front:
            self.rear = self.front = None
        else:
            self.front = self.front.left
            self.front.left = None
        return value

    def del_rear(self):
        if self.rear is None:
            return None
        value = self.rear.value
        if self.rear == self.front:
            self.rear = self.front = None
        else:
            self.rear = self.rear.right
            self.rear.left = None
        return value

    def reverse(self):
        curr = self.rear
        while curr:
            curr.left, curr.right = curr.right, curr.left
            curr = curr.left
        self.rear, self.front = self.front, self.rear

d = DEque()
for i in range(1, 6):
    d.insert_front(i)
    d.insert_rear(-i)
d.reverse()
for a in range(10):
    print(d.del_rear())
