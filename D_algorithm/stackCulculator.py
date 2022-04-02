class Operator:

    def __init__(self, op: str):
        self.op = op
        if op not in ('+', '-', '*', '/'):
            raise ValueError('사용가능한 연산자가 필요함')



    def __eq__(self, other):
        if type(other) != Operator:
            raise TypeError(f'{type(other)} 타입과 비교는 지원하지 않습니다....')

        if self.op in ('+', '-') and other.op in ('+', "-"):
            return True
        elif self.op in ('*', '/') and other.op in ('*', "/"):
            return True
        else:
            return False

    def __lt__(self, other):
        if type(other) != Operator:
            raise TypeError(f'{type(other)} 타입과 비교는 지원하지 않습니다....')
        return  self.op in ('+', '-') and other.op in ('*', "/")


    def __le__(self, other):
        if type(other) != Operator:
            raise TypeError(f'{type(other)} 타입과 비교는 지원하지 않습니다....')
        return self.__eq__(other) or self.__lt__(other)


    def __gt__(self, other):
        if type(other) != Operator:
            raise TypeError(f'{type(other)} 타입과 비교는 지원하지 않습니다....')

        return not self.__le__(other)


    def __ge__(self, other):
        if type(other) != Operator:
            raise TypeError(f'{type(other)} 타입과 비교는 지원하지 않습니다....')
        return not self.__lt__(other)
    #클래스 정보을 표현
    def __repr__(self):
        return  f'Operator({self.op})'

    def operation(self, X, Y):
        if self.op == '+':
            return X + Y
        elif self.op == '-':
            return X - Y
        elif self.op == '*':
            return X * Y
        elif self.op == '/':
            return X / Y


class IntCalcurator:

    def __init__(self):
        self.infix_expr = []

    def set_expression(self, expr: str):
        self.infix_expr.clear()
        operand = ''
        for x in expr:
            if x.isdigit():
                operand += x
            else:
                if len(operand) > 0:
                    self.infix_expr.append(int(operand))
                    operand = ''
                self.infix_expr.append(Operator(x))

        if len(operand) > 0:
            self.infix_expr.append(int(operand))
        print('수식율 리스트로:', self.infix_expr)

    #infix prefix로 표현ㅎㅏ는거
    # 1st. 숫자는 그래도 출력
    # 2nd. 연산자는 스택에 넣어야함
    #   2-1 스택이 비어있는 경우 무족건 넣는다
    #   2-2 스택이 비어있지 않으면 넣으려는 연산자와 스택에 있는 연산자 비교후 스택에 있는 연산자의 우선순위가 넣으려는 우선순위보다 작을때까지 스택에서 Pop하며 출력하고 넣으려는 연산자를 스택에 넣는다
    # 3rd. 마지막으로 남아있는 스택에 연산자를 출력함
    def infix_to_prefix(self):
        stack =[]
        prefix_expr =[]
        # 기능
        for c in self.infix_expr:
            if type(c) == int:
                prefix_expr.append(c)
            else:
                while len(stack) > 0 and stack[-1] > c:
                    prefix_expr.append(stack.pop())
                stack.append(c)
        while len(stack) > 0:
            prefix_expr.append(stack.pop())
        print('후위연산자 변환:', prefix_expr)
        return prefix_expr

    def evlution(self):
        prefix_expr = self.infix_to_prefix()
        stack = []
        for x in prefix_expr:
            if type(x) == int:
                stack.append(x)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(x.operation(operand1, operand2))

        if len(stack) > 1:
            raise ValueError('잘못된 수식을 계산하려했음')
        return stack.pop()
calc = IntCalcurator()
calc.set_expression('12*20-3+4')
print(calc.evlution())
