def solution(cacheSize, cities):
    answer = 0
    cach_list = []
    for i in cities:

        if cacheSize != 0:
            if i.lower() in cach_list:
                for k in range(len(cach_list)):
                    if i.lower() == cach_list[k]:
                        answer += 1
                        break
                del cach_list[k]
                cach_list.append(i.lower())

            else:
                if len(cach_list) < cacheSize:
                    cach_list.append(i.lower())
                else:
                    del cach_list[0]
                    cach_list.append(i.lower())
                answer += 5
        else:
            answer += 5

    return answer


print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
      "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))

# finish
