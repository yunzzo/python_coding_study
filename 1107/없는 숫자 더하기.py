def solution(numbers):
    numbers = sorted(numbers)
    compare =0
    sum_num =0
    for i in numbers:
        print(sum_num,compare,i)
        if compare != i:
            for j in range(compare,i):
                sum_num += j
            compare = i+1
        else:
            compare+=1
    for k in range(i+1,10):
        sum_num+=k  
    return sum_num

print(solution([5,8,4,0,6,7,9]))