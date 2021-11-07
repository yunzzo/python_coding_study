import heapq

def solution(n, works):
    for i in range(len(works)):
        works[i] *= -1
    heapq.heapify(works)

    for i in range(0, n):
        max_ele = heapq.heappop(works)
        if max_ele >= 0:
            heapq.heappush(works, max_ele)
            break
        max_ele += 1
        heapq.heappush(works, max_ele)
    tired = 0
    result = []
    while len(works) > 0:
        ele = heapq.heappop(works)
        result.append(ele * -1)
        tired += pow(ele * -1, 2)
    return tired,result

works = list(map(int, input("enter work load >> ").split())) 
N = int(input("enter remaining work times >> "))
tired, result = solution(N,works)
print(result,N,tired)
