import copy

def intersection(list1, list2):
    cnt = 0
    list3 = copy.copy(list2)
    for i in list1:
        if i in list3:
            list3.remove(i)
            cnt+=1
    return cnt

def solution(str1, str2):
    list1 = []
    list2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            list1.append(str1.lower()[i]+str1.lower()[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            list2.append(str2.lower()[i]+str2.lower()[i+1])
    gyo = intersection(list1, list2)
    if (gyo == 0) and (len(list1)+len(list2)-gyo) == 0:
        answer = 1
    else:
        answer = gyo / (len(list1)+len(list2)-gyo)
    return int(answer * 65536)
