def solution(board, moves):
    answer = 0
    basket=[]
    
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                #바구니에 넣어주기
                basket.append(board[i][move-1])
                #바구니 안 인형이 연속되는 지 검사
                if basket.count(board[i][move-1]) == 2:
                    print("인형 여러개!",board[i][move-1])
                #그 중복 인형들의 인덱스 위치 찾아서 저장
                    doll_indexs=list(filter(lambda x: basket[x]==board[i][move-1], range(0,len(basket))))
                    print("doll_indexs:",doll_indexs)
                    #차가 1이라면 연속된다는 의미
                    if abs(doll_indexs[1] - doll_indexs[0]) == 1:
                        print("연속 된 인형들 발견!")
                        #바구니에서 제거
                        """
                        이렇게 쓰면 리스트 인덱스 오류
                        del basket[doll_indexs[0]]
                        del basket[doll_indexs[1]]
                        
                        """
                        basket.remove(board[i][move-1])
                        basket.remove(board[i][move-1])
                        # +2해줘야하는데 이것때문에 계속 틀림
                        # answer=answer+1
                        print("answer:",answer)
                #인형을 뽑으면 0을 대입해서 빈공간으로 만들기
                board[i][move-1]=0
                break;
            
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))