"""
03시 13시 23시 => 3600개 
그 외 나머지 시간의 경우 =>900 + 675 =1575
확통문제 푸는 것 같았다! 그래서 위 식 구할때까지  삽질 엄청 함
"""

n=int(input())
result=0

for i in range(0,n+1):
    print(i)
    if i == (3 or 13 or 23):
        result+=3600
    else:
        result+=1575
        

print(result)