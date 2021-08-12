def solution(new_id):
answer=new_id
#대문자화
answer = answer.lower()
#제거할 문자들 
trash="~!@#$%^&*()=+[{]}:?,<>/"
    
for x in range(len(trash)):
    answer=answer.replace(trash[x],"")


#3단계 연속된 닷 제거
#replace문 활용
trash_dot=["."*x for x in range(15,1,-1)]
for i in trash_dot:
    answer=answer.replace(i,".")
print("3단계",answer)

#4단계 양쪽에 있는 "."들 제거
answer=answer.strip(".")
print("4단계",answer)
#5단계 빈문자열
if len(answer)==0:
    answer+="a"
print("5단계",answer)    
#6단계 
if len(answer)>15:
    answer=answer[:15]
    answer=answer.strip(".")
print("6단계",answer)       
#7단계
if len(answer)<=2:
    while ( len(answer) !=3 ):
        answer+=answer[-1]
print("7단계",answer)