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

# def push(stack,item):
#     stack.append(item)

# def pop(stack):
#     if len(stack) != 0:
#         item = stack.pop(-1)
#         return item
#     else:
#         empty()
# def empty():
#     print("Stack is Emplty")
# def top(stack):
#     if len(stack) != 0 :
#         return stack[-1]
#     else:
#         empty()
