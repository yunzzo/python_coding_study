def solution(lottos, win_nums):
    high = 0
    low = 0
    zero = []
    answer = []
    for i in range(len(lottos)):
        if lottos[i] == 0:
            zero.append(0)
        for j in range(len(win_nums)):
            if win_nums[j] == lottos[i]:
                low += 1
    high = low + len(zero)
    if high <= 1:
        answer.append(6)
    else:
        answer.append(7-high)
    if low <= 1:
        answer.append(6)
    else:
        answer.append(7-low)
    return answer


print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))