def solution(numbers):
    total = []
    for i in range(0,10):
        total.append(i)
    List = list(set(total)-set(numbers))
    answer = sum(List)
    
    return answer
