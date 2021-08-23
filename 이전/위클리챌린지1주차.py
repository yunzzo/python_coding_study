price = 3
money = 20
count = 4
result = 10


def solution(price, money, count):
    result = 0
    for i in range(count):
        result += price * (i+1)
    answer = result - money
    if(answer <= 0):
        answer = 0
    return answer


print(solution(price, money, count))
