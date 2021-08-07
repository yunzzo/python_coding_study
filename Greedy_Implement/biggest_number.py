#입력과 선언
n,m,k=map(int,input("숫자 세 개를 입력하세요(공백기준으로 나눔):").split())
data=list(map(int,input().split()))
#근데, N개의 수를 입력 받을 때, N개의 수를 초과하거나 그보다 적을 때 경고 문구를 띄우며 다시 입력받는 기능까지 구현해야 완벽한 것 아닌가? 구현해보자!


#처리
data.sort()
biggest_number=data[n-1]
second_number=data[n-2]
sum=0

while True:
    for i in range(k):
        if m==0:
            break
        sum+=biggest_number
        m-=1
    if m==0:
        break
    sum+=second_number
    m-=1
    


#출력
print(sum)