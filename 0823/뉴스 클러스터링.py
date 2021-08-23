def solution(str1, str2):
    liststr1 = []
    liststr2 = []

    for i in range(len(str1)-1):
        string = str1[i]+str1[i+1]
        if string.isalpha():
            liststr1.append(string.lower())

    for i in range(len(str2)-1):
        string = str2[i]+str2[i+1]
        if string.isalpha():
            liststr2.append(string.lower())
    print(liststr1, liststr2)
    inter = len([liststr1.remove(x) for x in liststr2 if x in liststr1])
    uni = len(liststr1 + liststr2)

    if uni == 0:
        return 65536

    return int(inter/uni * 65536)


print(solution("aa1+aa2",  "AAAA12"))
