def solution(cacheSize, cities):
    answer = 0
    cach_list = []
    for i in cities:
        if cacheSize != 0:
            if i.lower() in cach_list:
                answer += 1
            else:
                answer += 5
            if len(cach_list) < cacheSize:
                cach_list.append(i.lower())
            else:
                del cach_list[0]
                cach_list.append(i.lower())
        else:
            answer += 5

    return answer


print(solution(2, 	["Jeju", "Pangyo", "NewYork", "newyork"]))
