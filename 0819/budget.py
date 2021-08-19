def solution(d, budget):
    cnt = 0
    total = 0
    d.sort()
    for i in range(len(d)):
        total += d[i]
        if total > budget:
            break
        cnt += 1
    return cnt