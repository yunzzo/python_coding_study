def palindrom(data:str)->bool:
    string_list = []
    for chr in data:
        if chr.isalpha():
            string_list.append(chr.lower())
    print(string_list)
    while len(string_list) >1:
        if string_list.pop(0) != string_list.pop():
            return False
    return True

import collections

def palindrom_deq(data):
    string_list = collections.deque()
    for chr in data:
        if chr.isalpha():
            string_list.append(chr.lower())
    print(string_list)
    while len(string_list) >1:
        if string_list.popleft() != string_list.pop():
            return False
    return True

if __name__ == '__main__':
    data = input('input string::')
    print(f'{palindrom_deq(data)}')