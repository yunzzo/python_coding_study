lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]


def solution(lottos, win_nums):
    zero_cnt = 0
    rate_cnt = 0
    best = 0
    rate = 0
    answer = []
    for lotto_num in lottos:
        if lotto_num == 0:
            zero_cnt += 1
        elif lotto_num in win_nums:
            rate_cnt += 1
    best = rate_cnt + zero_cnt
    rate = 7 - best
    if (rate == 7):
        rate = 6
    answer.append(rate)
    rate = 7 - rate_cnt
    if (rate == 7):
        rate = 6
    answer.append(rate)
    return answer


print(solution(lottos, win_nums))
