import sys

size = int(sys.stdin.readline())
arr = [0] * size
for i in range(size):
    arr[i] = int(sys.stdin.readline())


def maxCroSub(arr, first, middle, last):
    leftSum = float("-inf")
    sum = 0
    maxLeft = middle
    maxRight = middle+1
    for i in range(middle, first-1, -1):
        sum = sum + arr[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i
    rightSum = float("-inf")
    sum = 0
    for j in range(middle+1, last+1):
        sum = sum + arr[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j
    return [maxLeft, maxRight, leftSum+rightSum]


def maxsub(arr, first, last):
    if(first == last):
        return [first, last, arr[first]]
    else:
        middle = (first + last) // 2
        [lFirst, lLast, lSum] = maxsub(arr, first, middle)
        [rFirst, rLast, rSum] = maxsub(arr, middle + 1, last)
        [cFirst, cLast, cSum] = maxCroSub(arr, first, middle, last)
        if lSum >= rSum and lSum >= cSum:
            return [lFirst, lLast, lSum]
        elif rSum >= lSum and rSum >= cSum:
            return [rFirst, rLast, rSum]
        else:
            return [cFirst, cLast, cSum]


result = maxsub(arr, 0, size-1)
s = ""
for i in result:
    s += (str(i) + '\n')
print(s)
