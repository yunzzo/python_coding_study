def solution(record):
    #딕셔너리 안쓰고 리스트로 반복문 돌리면서 했는데 시간초과 런타임에러 엄청 떠서 질문하기에서 딕셔너리 자료형활용하는거 엿봤습니다^^ 근데 구조적으로는 동일했다;;
    answer = [] 
    id_nicknames={}

    for i in record:
        i=i.split()
        #길이가 3이면 무조건 change 아니면 enter
        if len(i)==3: 
            id_nicknames[i[1]]=i[2]
        #leave 면 아이디, 닉네임쌍 변경할 필요 없음
    
    #출력
    for i in record:
        i=i.split()
        
        if i[0] == "Enter":
            answer.append(f"{id_nicknames[i[1]]}님이 들어왔습니다.")
        elif i[0] == "Leave":
            answer.append(f"{id_nicknames[i[1]]}님이 나갔습니다.")



    return answer