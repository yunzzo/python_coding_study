def prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def solution(nums):
    total =[]
    from itertools import combinations
    comb = list(combinations(nums, 3))
    for i in range(len(comb)):
        total.append(comb[i][0]+comb[i][1] + comb[i][2])
    cnt =0
    for i in range(len(total)):
        if prime(total[i]):
            cnt += 1
    return cnt


print(solution([1,2,7,6,4]))