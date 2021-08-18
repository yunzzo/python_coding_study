def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        j=i+1
        while(j < len(numbers)):
            if numbers[i]+numbers[j] in answer:
                j+=1
                continue
            else:
                answer.append(numbers[i]+numbers[j])
                j+=1
    answer.sort()
    return answer

print(solution([2,1,3,4,1]))