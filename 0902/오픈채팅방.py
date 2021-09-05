def solution(record):
    result = []
    e = {}
    for re_ele in record:
        doList = re_ele.split(' ')
        result.append((doList[0], doList[1]))
        if len(doList) > 2:
            e[doList[1]] = doList[2]
    answer = []
    for ele in result:
        if ele[0] == 'Enter':
            answer.append(e[ele[1]]+'님이 들어왔습니다.')
        elif ele[0] == 'Leave':
            answer.append(e[ele[1]]+'님이 나갔습니다.')
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234",
      "Enter uid1234 Prodo", "Change uid4567 Ryan"]))

# finish
