from itertools import combinations


def solution(relation):
    key = []

    for i in range(1, len(relation[0])+1):

        for com in list(combinations(range(len(relation[0])), i)):

            isin = 0
            compare = set()

            for item in relation:
                compare_item = []
                for e in com:

                    compare_item.append(item[e])
                compare.add(tuple(compare_item))
            if len(compare) == len(relation):
                for ii in key:
                    if (set(ii) & set(com)) == set(ii):
                        isin = 1
                        break
                if isin == 0:
                    key.append(com)

    return len(key)

# finish


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], [
      "400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
