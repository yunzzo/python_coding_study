def solution(msg):
    answer = []
    diction = {}
    for i in range(1, 27):
        diction[chr(i+64)] = i
    index = 27
    doindex = -1
    for msg_num in range(len(msg)):

        testword = ""
        prevword = ""
        if msg_num <= doindex:
            continue
        for i in range(msg_num, len(msg)):
            testword += msg[i]
            if i > msg_num:
                prevword += msg[i-1]
            if testword not in diction:
                doindex = i-1
                diction[testword] = index
                answer.append(diction[prevword])
                index += 1
                break
            if i == len(msg)-1:
                doindex = i
                answer.append(diction[testword])
                index += 1
                break

    return answer
# finish


print(solution(	"TOBEORNOTTOBEORTOBEORNOT"))
