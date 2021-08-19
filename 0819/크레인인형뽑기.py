#테스트 모두 통과 못함
def solution(board, moves):
    answer = 0
    basket=[]
    for move in moves:
        for i in range(len(board)):
            #인형을 뽑으면
            if board[i][move-1] != 0:
                #바구니에 넣어주기
                basket.append(board[i][move-1])
                #바구니 안 인형이 연속되는 지 검사
                doll_index=len(basket)-1
                if (doll_index-1 >=0) and basket[doll_index-1] == basket[doll_index] :               
                        #바구니에서 그 인형 제거
                        #basket.remove(board[i][move-1])
                        #basket.removbasketd[i][move-1])                     
                        #del basket[doll_index-1]
                        #del basket[doll_index]
                        while board[i][move-1] in basket:    
	                        basket.remove(board[i][move-1])
                        answer+=2          
                #인형을 뽑으면 0을 대입해서 빈공간으로 만들기
                board[i][move-1]=0
                break;
            
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))

