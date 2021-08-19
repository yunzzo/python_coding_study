def solution(d, budget):
    answer = 0
    d.sort()
    mybudget = 0
    for i in range(len(d)):
        answer += 1
        mybudget += d[i]
        if mybudget > budget:
            answer -= 1
            break
    return answer


print(solution([1, 3, 2, 5, 4], 9))
