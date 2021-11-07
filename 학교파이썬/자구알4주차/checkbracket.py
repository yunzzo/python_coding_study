def checkBracket(words):
    stack = []
    open = '[{('
    close = ']})'
    for word in words:
        if word in open:
            stack.append((word, open.index(word)))
        elif word in close:
            if stack[-1][1] == close.index(word):
                stack.pop()
            else:
                return False
    if len(stack) == 0 :
        return True
    else:
        return False
if __name__ == '__main__':
    print(checkBracket(input()))
