def solution(sizes):
    sizes.sort()
    print(sizes)
    for i in range(len(sizes)):
        for j in range(i+1, len(sizes)):
            if sizes[i][0] >= sizes[j][1]:
                width = sizes[i][0]
                print(width)
            else:
                break

solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
