class Stack:
    def __init__(self, size):
        self.data = []
        self.size = size

    def isEmpty(self):
        return len(self.data) == 0

    def isFull(self):
        return len(self.data) == self.size

    def push(self, value):
        if not self.isFull():
            self.data.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.data.pop()

    def peek(self):
        if not self.isEmpty():
            return self.data[-1]
def Mid2Post(express):
    s = Stack(20)
    result = []
    for i in express:
        if i in '(':
            s.push(')')
        elif i in ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':break
                else: result.append(op)
        elif i in '+-*/':
            while not s.isEmpty():
                op = s.peek()
                if(precedence(i)<=precedence(op)):
                    result.append(op)
                    s.pop()
                else:
                    break
            s.push(i)
        


def PostResult(express):
    s = Stack(20)
    for i in express:
        if i == '+':
            a = s.pop()
            b = s.pop()
            s.push(a+b)
        elif i == '-':
            a = s.pop()
            b = s.pop()
            s.push(a-b)
        elif i == '*':
            a = s.pop()
            b = s.pop()
            s.push(a*b)
        elif i == '/':
            a = s.pop()
            b = s.pop()
            s.push(int(a/b))
        else:
            s.push(int(i))
    return s.pop()


if __name__ == '__main__':
    express = input("enter your expression >> ")
    print(PostResult(express))
