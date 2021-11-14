import numpy as np
def solution(info, query):
    # 리스트 생성
    i = [x.split(' ') for x in info]
    q = [x.replace(" and", "").split(' ') for x in query]

    for n in range(len(q)):
        temp = []
        for m in range(len(i)):
            if q[n][:4] == i[m][:4] and i[m][4] >= q[n][4]:
               temp += i[m]
               # '-'는 어떻게 고려하는지

        print(temp)
    print(len(q))
    return 

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
        , ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])