N = 4
stages = [4, 4, 4, 4, 4]


def solution(N, stages):
    failrate = [[i, 0] for i in range(N)]
    answer = []
    reach = [0 for _ in range(N)]
    notyet = [0 for _ in range(N)]

    for i in range(len(stages)):
        for k in range(stages[i]-1):
            reach[k] += 1
        if stages[i]-1 != N:
            notyet[stages[i]-1] += 1
            reach[stages[i]-1] += 1

    for i in range(N):
        if reach[i] != 0:
            failrate[i][1] = notyet[i] / reach[i]

    failrate.sort(key=lambda x: (-x[1], x[0]))

    for i in failrate:
        answer.append(i[0]+1)

    return answer


solution(N, stages)
