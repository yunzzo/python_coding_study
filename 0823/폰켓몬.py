def solution(nums):
    answer = 0
    half = len(nums)//2
    num_class = len(set(nums))
    if half >= num_class:
        answer = num_class
    else:
        answer = half
    return answer


print(solution([3, 1, 2, 3]))
