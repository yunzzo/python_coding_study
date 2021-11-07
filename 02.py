import math

def solution(n):
    x = n-1
    if x % 2 == 0:
        return 2
    else:
        for i in range(2, int(math.sqrt(x)+1)):
            if x % i == 0:
                return i
    return x


"""
import math

def solution(n):
    x = n-1
    if x % 2 == 0:
        answer = 2
    else:
        for i in range(2, int(math.sqrt(x)+1)):
            if x % i == 0:
                answer = i
            else:
                answer = x
    return answer
"""