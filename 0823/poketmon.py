def solution(nums):
    different = []
    for i in range(len(nums)):
        if nums[i] not in different:
            different.append(nums[i])
    return min(len(nums)/2, len(different))

