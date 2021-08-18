def solution(a, b):
    plus = []
    answer = 0
    total = list(zip(a, b))
    for i in range(len(total)):
        plus.append(total[i][0] * total[i][1])
    for i in range(len(plus)):
        answer += plus[i]

    return answer
