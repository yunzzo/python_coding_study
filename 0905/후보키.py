import itertools

"""
단독으로 후보키가 될 수 있는 속성이면, 2개 3개 조합의 후보키 속성이 될 수 없다. 
그래서, 후보키로 판명된다면 후보키의 개수를 증가시키고, relation에서 그 속성줄을 전체 제거해준다. 
이렇게 했는데, 5개 정도만 통과하고 인덱스에러 계속 남
extend append


"""
def solution(relation):
    #relation 가로 세로 바꿔주기
    relation=list(map(list,zip(*relation)))
    answer = 0
    keys=[]
    temp=[]
    #속성 단독 후보 키 조사
    k=1
    while k <= len(relation):
        #어트리부트(속성의 개수만큼) 
        attributes=[x for x in range(0,len(relation))]
        #컴비네이션 만들기
        combi=list(itertools.combinations(attributes,k))
        #요소의 개수만큼
        temp=[[] for _ in range(len(relation[0]))]
        for i in combi: #[(0,), (1,), (2,), (3,)]
            for t in i: 
                for j in range(0,len(relation[0])): #실제 인덱스 0~5
                    #이렇게 하면 문자열 더하기 구현할 수 있음(근데 아까도 문자열더했다가 문제) 문자열더하기X
                    temp[j].extend([relation[t][j]])
            #후보키가 될 수 있는지 검사
            if len(temp) ==  len(set(list(map(tuple,temp)))):
                
                answer+=1
                #keys에 담기
                for key in i:
                    keys.extend([i])
            temp=[[] for _ in range(len(relation[0]))]
            
        #삭제해주기(후보키가 된 속성의 줄을 모두 삭제)
        for i in set(keys):
            for k in i:
                del relation[k] 
        k+=1
        keys=[]
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))