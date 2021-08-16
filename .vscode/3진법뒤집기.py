n = 45


def solution(n):
    num3 = ''
    while n > 0:
        n, mod = divmod(n, 3)
        num3 += str(mod)
    answer = int(num3, 3)
    return answer


print(solution(n))
