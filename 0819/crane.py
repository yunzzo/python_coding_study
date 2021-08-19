def solution(board, moves):
    answer = 0
    blank =[]
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                blank.append(board[j][moves[i]-1])
                board[j][moves[i] - 1] = 0
                break
    k=0
    print(blank)
    while(k<len(blank)-1):
        if blank[k] == blank[k+1]:
            del blank[k]
            del blank[k]
            print(blank)
            answer += 2
            k=0
        else:
            k += 1
    return answer

#
# print(solution([[0,0,0,0,0],
#                 [0,0,1,0,3],
#                 [0,2,5,0,1],
#                 [4,2,4,4,2],
#                 [3,5,1,3,1]],
#                [1,5,3,5,1,2,1,4]))