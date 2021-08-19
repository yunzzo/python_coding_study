import itertools


def solution(nums):
    answer = 0
    myset = []
    result = list(itertools.combinations(nums, 3))
    for (a, b, c) in result:
        myset.append(a+b+c)
    for ele in myset:
        count = 0
        for i in range(2, ele//2 + 1):
            if ele % i == 0:
                count += 1
        if count == 0:
            answer += 1
    return answer


print(solution([1, 2, 7, 6, 4]))
