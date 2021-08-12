#입력과 선언
n,m=map(int, input("행 렬을 입력하세요:").split())
result=0

#처리(근데, 여전히 렬의 갯수를 포괄하지 못함, 정해진 렬보다 많이 입력했을 경우를!)
for i in range(n):
    data=list(map(int,input("숫자를 입력하세요:").split()))    
    min_number=min(data)
    result=max(result, min_number)



#출력
print(f"가장 큰 수는 {result}입니다.")

#1 입력할 때 한계 여전히 존재
#2 가장 큰 수를 뽑는 경우는, n행의 r렬이다라는 식으로 구체적으로 결과를 특정할 수 있어야할 것 같은데?