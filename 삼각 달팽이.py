def solution(n):
    answer = []
    level = [[]for _ in range(n)]
    num = 1
    index = 0
    state = 1
    max = n
    min = 0
    while True:
        if state == 1:
            level[index].append(num)
            if index == n - 1:
                state = 0
                max -= 1
                if index < 0:
                    break
            else:
                index += 1
            num += 1
        else:
            level[index].append(num)
            if index == min+1:
                state = 1
                index += 1
                min += 1

            else:
                index -= 1
            num += 1

    return level


print(solution(4))
