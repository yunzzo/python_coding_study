# def head_insert(s,item):
#     if s == []:
#         s.append(item)
#     else:
#         s.append(None)
#         size = len(s)
#         for i in range(size, 1, -1):
#             s[i-1] = s[i-2]
#         s[0] = item

# def insert_after(s,item, p):
#     if p == len(s) -1:
#         s.append(item)
#     else:
#         s.append(None)
#         size = len(s)
#         for i in range(size,p+1,-1):
#             s[i-1] = s[i-2]
#         s[p] = item

# def delete(s,p):
#     if s==[]:
#         print("Error")
#     elif p >= len(s) or p<0:
#         print("Error")
#     elif len(s) == p+1:
#         del s[p]
#     else:
#         size = len(s)
#         for i in range(p,size-1):
#             s[i] = s[i+1]
#         del s[i+1]
    

# if __name__ == '__main__':
#     fruit = []
#     head_insert(fruit,'orange')
#     head_insert(fruit,'cherry')
#     head_insert(fruit,'banana')
#     head_insert(fruit,'blueberry')
#     insert_after(fruit,'apple',1)
#     insert_after(fruit,'pear',0)
#     delete(fruit,2)
#     print(fruit)

class ArrayList:
    def __init__(self):
        self.data = []
    def isEmpty(self):
        if len(self.data) == 0:
            return True
    def head_insert(self, value):
        if self.data == []:
            self.data.append(value)
        else:
            size = len(self.data)
            self.data.append(self.data[-1])
            for i in range(size,1,-1):
                self.data[i-1] = self.data[i-2]
            self.data[0] = value
    def insert_after(self, value, p):
        if p == len(self.data)-1:
            self.data.append(value)
        else:
            size = len(self.data)
            self.data.append(self.data[-1])
            for i in range(size, p+1, -1):
                self.data[i-1] = self.data[i-2]
            self.data[p] = value
    def delete_self(self,p):
        if self.isEmpty():
            print(f'list is Empty')
        else:
            self.data.pop(p)
    def display(self):
        print(f'List Items:{self.data}')

if __name__ == "__main__":
    fruit = ArrayList()
    animal = ArrayList()
    fruit.head_insert('apple')
    fruit.head_insert('mango')
    fruit.insert_after('pear',1)
    fruit.display()
    animal.head_insert('cat')
    animal.insert_after('dog',1)
    animal.insert_after('tiger',0)
    animal.display()