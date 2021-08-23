def solution(m, n, board):
    count=0
    try_count=0
    """
    가로로 2줄씩 잘라서 검사 -> 삭제할 좌표 저장 -> 한바퀴 돌기 -> set써서 삭제할 블록 중복제거해서 구하기
    ->삭제로 배열 업데이트 -> 또 한바퀴 돌기(종료조건은 5번 다돌아도 2x2 못찾으면 종료)
    """
    del_lists=[]
    while True:
        for i in range(0, n-1):
            for j in rnage(0,m):
            #2x2면 좌표 저장
                if board[j][i] == board[j][i+1] and board[j][i] == board[j+1][i] and board[j][i] == board[j+1][i+1]:
                    del_lists+=[[j,i]] + [[j,i+1]]+[[j+1,i]]+[[j+1,i+1]]
                    try_count+=1
        #한바퀴를 다 돈 후, 중복제거 후 삭제할 인형들 갯수 세주고 삭제하기
        count+=len(set(del_lists))
        #del_lists를 높이가 높은 순부터 정렬한다음, 삭제해주면 정확하게 삭제        
        del_lists.sort(key=lambda x:x[1],reverse=True)
        for i in del_lists:
            del board[i[0]][i[1]]
        #종료 조건(5번 다 돌았는데, 2x2 못찾았으면 종료)
        if try_count ==0:
            break
    
    return count