from collections import deque


def jinbub(num, n):
    q = deque([])
    o = ''
    while num:
        num, m = divmod(num, n)
        o = (str(m) if m < 10 else 'ABCDEF'[m-10])+o
        q.appendleft(str(m) if m < 10 else 'ABCDEF'[m-10])

    return ''.join(q)


def solution(n, t, m, p):
    answer = '0'
    result = ""
    for i in range(1, 1000):
        answer += jinbub(i, n)
        if len(answer) > t * (2):
            break
    print(answer)
    index = 1
    for i in answer:
        print(answer, i, index)
        if (index - p) % m == 0:
            print(index)
            result += i
        if len(result) >= t:
            break
        index += 1

    return result


print(solution(	16, 16, 2, 1))
