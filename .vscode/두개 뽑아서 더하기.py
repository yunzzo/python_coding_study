numbers = [2, 0, 1]


def solution(numbers):
    s = set()
    for i in range(len(numbers)):
        for k in range(i+1, len(numbers)):
            s.add(numbers[i]+numbers[k])
            print(numbers[i], numbers[k])
    s = sorted(s)
    answer = list(s)
    return answer


print(solution(numbers))
