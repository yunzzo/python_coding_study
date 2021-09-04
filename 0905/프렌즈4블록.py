def solution(m, n, board):
    count=0
    board=list(map(list,zip(*board)))
    """
    board의 가로와 세로를 바꿔준다
    2x2로 위에서부터 아래로 내려가면서 조사
    삭제할 좌표를 새로운 리스트에 담아서, 그 좌표를 이용해 인형을 제거 
    리스트에서 삭제하게 되면, 인덱스와 길이 모두 바뀌어서 더 성가시게 되므로 삭제한 자리에 전혀 연관없는 문자를 대입해서 길이와 인덱스를 유지해준다.
    """
    while True:
        del_lists=[]
        try_count=0
        #가로부분   
        for j in range(0,len(board)-1):
            #세로부분
            for i in range(0,len(board[0])-1):            
            #2x2로 똑같은 인형들이 있으면, 그 인형들의 좌표 저장
                if board[j][i] != "0":
                    if board[j][i] == board[j][i+1] and board[j][i] == board[j+1][i] and board[j][i] == board[j+1][i+1]:
                        del_lists+=[(j,i)] + [(j,i+1)]+[(j+1,i)]+[(j+1,i+1)]
                        try_count+=1
        #종료 조건(한바퀴 돌았는데, 2x2 못찾았으면 종료)
        if try_count ==0:
            break
        #한바퀴를 다 돈 후, 삭제할 인형들 갯수 세주고, 삭제하기(중복제거를 해줘야 정확하게 인형갯수를 셀 수 있다)
        count+=len(set(del_lists))
        #del_lists를 정렬한다음 삭제해주면 정확하게 삭제        
        del_lists=list(set(del_lists))
        #정렬
        del_lists.sort(key=lambda x:x[1],reverse=True)
        #삭제
        for i in del_lists:
            del board[i[0]][i[1]] 
        #삭제해주면 길이가 달라져서, 인덱스에서 여러가지 문제 발생. 그래서 길이를 기존과 똑같이 유지해주기 위해서 "0"을 대입 
        for i in range(n):
            while len(board[i]) != m:
                board[i].insert(0,"0")
    return count        

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))