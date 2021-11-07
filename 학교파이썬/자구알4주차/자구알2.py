# 자신제외 나머지 의곱으로
# nums = list(input())
# index = 0
# mul = 1
# result = []
# for i, num in enumerate(nums):
#     num = nums[0:i] * nums[i:]
#     print(num)

from typing import List


def product(values: List[int]) -> List[int]:
    result = []
    new_result= []
    point = 1
    for i in range(len(values)):
        result.append(point)
        point *= values[i]
    point = 1
    for i in range(len(values)-1, -1, -1):
        result.append(point)
        point *= values[i]

    for i in range(len(result)//2):
        new_result.append(result[i]* result[len(result)-i-1])
    print(new_result)

if __name__ == '__main__':
    product([1,2,3,4])
