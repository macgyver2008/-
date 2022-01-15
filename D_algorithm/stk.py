class StackElement:

    def __init__(self, value, next):
        self.value = value
        self.next = next
class Stack:




    def __init__(self):
        self.top = None
        pass

    def push(self, value):
         if self.top == None:
             elem = StackElement(value, None)
             self.top = elem
         else:
             elem = StackElement(value, self.top)
             self.top = elem

    def pop(self):
        if self.top == None
            return None
        else:
            pop_elem = self.top
            self.top = self.top.next
            return pop_elem.value


    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.value


stk = Stack()
stk.push(1)
stk.push(2)
stk.push(3)
print(stk.pop())
print(stk.pop())
print(stk.pop())
print(stk.pop())
