scores = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [
    47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]

# 행렬을 전치시키는 게 이문제의 핵심 ,, enumerate 또는 zip사용법


def solution(scores):
    newscore = list(map(list, zip(*scores)))
    answer = ''
    for i in range(len(newscore)):
        sum = 0
        avg = 0
        cnt = 0
        minN = min(newscore[i])
        maxN = max(newscore[i])
        for k in newscore[i]:
            sum += k
            if minN == newscore[i][i] and minN == k:
                cnt += 1
            if maxN == newscore[i][i] and maxN == k:
                cnt += 1
        if (minN == newscore[i][i] or maxN == newscore[i][i]) and cnt == 1:
            sum -= newscore[i][i]
            avg = sum / (len(newscore)-1)
        else:
            avg = sum / len(newscore)
        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer


print(solution(scores))
