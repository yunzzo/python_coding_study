n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


def solution(n, arr1, arr2):
    map1 = [[] for _ in range(n)]
    map2 = [[] for _ in range(n)]
    map_final = [[] for _ in range(n)]
    for i in range(n):
        map1[i] = format(arr1[i], '0' + str(n)+'b')
    for i in range(n):
        map2[i] = format(arr2[i], '0' + str(n)+'b')
    for i in range(n):
        map_row = ''
        for k in range(n):
            if map1[i][k] == '0' and map2[i][k] == '0':
                map_row += " "
            else:
                map_row += "#"
        map_final[i] = map_row
    return map_final


solution(n, arr1, arr2)
