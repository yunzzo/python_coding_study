dartResult = input()


def solution(dartResult):
    dartNum = 0
    dartBonus = ''
    dartResultList = [0 for _ in range(3)]
    dartCount = 0
    answer = 0
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if i != 0 and dartResult[i-1].isalpha():
                dartResultList[dartCount] += dartNum**dartBonus
                dartCount += 1
            dartNum = int(dartResult[i])
            if i != 0 and dartResult[i-1].isdigit():
                dartNum = 10
        if dartResult[i].isalpha():
            if dartResult[i] == 'S':
                dartBonus = 1
            elif dartResult[i] == 'D':
                dartBonus = 2
            elif dartResult[i] == 'T':
                dartBonus = 3
            if i == len(dartResult)-1:
                dartResultList[dartCount] += dartNum**dartBonus
        if dartResult[i] == '*' or dartResult[i] == '#':
            if dartResult[i] == '*':
                if dartCount != 0:
                    dartResultList[dartCount-1] *= 2
                dartResultList[dartCount] += (dartNum**dartBonus) * 2
            elif dartResult[i] == '#':
                dartResultList[dartCount] += (dartNum**dartBonus) * (-1)

            dartCount += 1

    for i in dartResultList:
        answer += i

    return answer


print(solution(dartResult))
