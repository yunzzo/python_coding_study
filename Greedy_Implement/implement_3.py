"""
알파벳 정렬 sort나 sorted 함수 사용

숫자인지 알파벳인지 검사해주는 함수 사용

알파벳이면 알파벳 리스트에 저장 후 정렬 함수 사용
숫자는 그때그때 더해서 결과도출

문자열 더하기해서 출력
"""
#입력
n=input()
sum=0
list=[]
result=""


#처리
str_len=len(n)
for i in range(str_len):
    if n[i].isupper() ==True:
        list.append(n[i])
    else:
        sum+=int(n[i])
#정렬
list.sort()

#리스트 문자열로 바꿔주기
for i in range(len(list)):
    result+=list[i]

result+=str(sum)

#출력
print(result)

