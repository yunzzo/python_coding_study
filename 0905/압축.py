import string 

def solution(msg):
    #초기화
    #가장 긴 단어를 담을 변수
    longest_words=""
    #정답변수
    answer = []
    #알파벳 모두
    keys=string.ascii_uppercase  
    #딕셔너리 자료형
    dic={}
    #딕셔너리 알파벳으로 초기화 해주기
    for i in range(1,27):
        dic[keys[i-1]]=i
    #키가 알파벳 밸류가 색인
    #현재 입력과 일치하는 가장 긴 문자열 찾기
    while True:
        #종료조건, 문자열 길이가 0일때와 1일때 다르게 처리를 해줘야되서 분리
        if len(msg) ==0:
            break
        if len(msg) ==1:
            answer.append(dic[msg[0]])
            break 
        #가장 긴 문자열 찾기
        for k in range(1,len(msg)+1):
            temp=msg[0:k]
            #longest_words에는 가장 긴 문자열이 담기게 된다
            if temp in dic.keys():
                longest_words=temp

        #answer에 가장 긴 문자열의 색인을 저장
        answer.append(dic[longest_words])
        #입력에서 가장 긴 문자열 제거(이게 문자열에서 문자를 제거하려고 하면, 어떻게든 중복되는 문자가 모두 삭제되어서 리스트로 바꿔서 삭제 그리고 다시 문자열로 변환)
        msg=list(msg)
        for _ in range(0,len(longest_words)):
            del msg[0]
        
        #다시 문자열 자료형으로 바꿔주기
        msg="".join(msg)    

        #다음 글자까지 사전에 등록하는 과정
        if len(msg)>=1:
            longest_words=longest_words + msg[0]
            #사전에 추가
            dic[longest_words]=len(dic)+1
        #초기화 
        longest_words=""
    return answer

print(solution("ABABABABABABABAB"))