#프로그래머스 레벨 1 신규 아이디 추천
"""
여기서는 문자열 자료형에 대해서 많이 배울 수 있었다.
특히, 2, 3단계에서 배울 점이 있었다.

replace함수가 되게 유용했는데, 이를 이용해서, 문자열 내에서 특정 문자를 제거하거나,
원하는 요소로 바꿀 수 있다.
replace함수를 2단계 코드처럼 사용할 수 있었던 이유는, replace함수의 첫번째 피라미터로
들어가는 인자가, 대상 문자열에 실제로 없더라도, 오류를 발생시키지 않기 때문이다. 
""" 

def solution(new_id):
    trash="~!@#$%^&*()=+[{]}    :?,<>/"
    answer=new_id
    #1단계
    #소문자화
    answer = answer.lower()
    
    #2단계
    #제거할 문자들 

    #문자들 제거
    for x in range(len(trash)):
        answer=answer.replace(trash[x],"")
        
    #3단계 연속된
    #replace문 활용(여기까지 문제 없음)
    trash_dot=["."*x for x in range(15,1,-1) ]
    for i in trash_dot:
        answer=answer.replace(i,".")
        
    #4단계 양쪽에 있는 "."들 제거
    answer=answer.strip(".")
    
    #5단계 빈문자열
    if len(answer)==0:
        answer+="a"
    
    #6단계 
    if len(answer)>15:
        answer=answer[:15]
        answer=answer.strip(".")
        
    #7단계
    if len(answer)<=2:
        while ( len(answer) !=3 ):
            answer+=answer[-1]
    
    return answer