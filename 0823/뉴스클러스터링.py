def solution(str1, str2):
    answer = 0
    #str1,str2를 담을 다중집합
    first=[]
    second=[]
    len_intersec=0
    len_union=0
    #소문자화
    str1=str1.lower()
    str2=str2.lower()
    #두 개씩 빼내기
    for i in range(0,len(str1)-1):
        #두 개가 알파벳이라면
        if (str1[i]+str1[i+1]).isalpha():
            first.append(str1[i]+str1[i+1])
    #str2도    
    for i in range(0,len(str2)-1):
        if (str2[i]+str2[i+1]).isalpha():
            second.append(str2[i]+str2[i+1])
    #집합자료형 새롭게 생성
    set_first=set(first)
    set_second=set(second)

    #그곳에서 교집합 찾아주기
    intersec=set_first & set_second
    #진짜 교집합,합집합의 수를 구하는 과정
    for i in intersec:
            len_union+=max(first.count(i),second.count(i))
            len_intersec+=min(first.count(i),second.count(i))
    #합집합 마지막으로 구하기(합집합-교집합의 수를 더해줘야함)
    len_union+=len( (set_first | set_second ) - intersec )
    #유사도 구하기
    if len_union==0:
        answer=1
    else:
        answer= len_intersec/len_union
        
    answer= int(answer*65536)
    return answer