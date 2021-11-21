def solution(info, query):
    answer = [0 for i in range(len(query))]
    # 리스트 생성
    i = [x.split(' ') for x in info]
    q = [x.replace(" and", "").split(' ') for x in query]

    for m in range(len(i)):
        for j in range(len(q)):
            c = 0
            for k in range(4):
                if i[m][k] != q[j][k]:
                    if q[j][k] != '-':
                        c = 1
                        break
            if c == 0:
                if int(i[m][4]) >= int(q[j][4]):
                    answer[j] += 1
    print(answer)
    return answer

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
        , ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])