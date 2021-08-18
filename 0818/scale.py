def solution(n):
    before = []
    answer = 0
    if n>=3:
        while (n>=3):
            before.append(n % 3)
            n = n // 3
            if n < 3:
                before.append(n)
    else:
        before.append(n)
    for i in range(len(before)):
        answer += before[i] * (3 ** (len(before) - 1 - i))
    return answer

