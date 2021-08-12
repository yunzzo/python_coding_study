def solution(N, stages):
    

    #먼저 정렬
    stages.sort()

    temp_list=[]
    answer=[]
    list=[]
    #각 단계
    for i in range(1,N+1):
        #실패율을 계산하기 위해서 분모 분자 
        bottom,top=0,0
        for j in stages:
            if i <= j:
                bottom +=1
            if i == j:
                top += 1   
        #실패율 계산
        fail= top / bottom 
        #빈 리스트에 실패율 저장
        temp_list.append(fail)   
        
        #2차원으로 단계랑 실패율 같이 저장
        point_and_fail=[i,fail]
        list.append(point_and_fail)
    
    #반복문을 다 돌면, 실패율이 계산되어 있음(인덱스랑 대응)
    #여기 어렵다
    #실패율을 오름차순으로 정리
    fail_list=sorted(temp_list) 
    fail_list.reverse()

    """"
    #여기부터 문제
    for i in  range(0,N):
        count=0
        for j in range(0,N):
            count+=1
            if fail_list[i] == temp_list[j]:         
                #아..
                if j<N-1:
                    if temp_list[j]==temp_list[j+1]:
                        continue
                answer.append(count)
                break
    """
    for i in fail_list:
        for j in list:
            if j[1] == i:
                answer.append(j[0])
                #찾고 그 요소 삭제
                del list[list.index(j)]
                break


    return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
#실패율 같은 경우 해결 못하는 중/ 그냥 다른 방법? -> 2차원 배열로 단계 같이 표시하면서 해결 가능 ㄱ


