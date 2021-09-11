def right(p):
    open = 0
    for i in p:
        if i == '(':
            open += 1
        elif i == ')':
            open -= 1
        if open < 0:
            return False
    if open == 0:
        return True


def parell(p):
    open = 0
    for i in p:
        if i == '(':
            open += 1
        elif i == ')':
            open -= 1
    if open == 0:
        return True
    else:
        return False


def modify(p):
    answer = ""
    for i in p[1:-1]:
        if i == '(':
            answer += ')'
        elif i == ')':
            answer += '('
    return answer


def solution(p):

    u = ''
    v = ''
    if right(p):
        return p
    for ele in range(len(p)):
        u += p[ele]
        if parell(u):
            v = p[ele+1:]
            if right(u):
                string = solution(v)
                return u+string
            else:
                string = '('+solution(v)+')'+modify(u)
                return string


print(solution("()))((()"))
