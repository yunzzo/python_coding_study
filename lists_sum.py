#프로그래머스 레벨1 내적
def solution(a, b):
    answer = 0
    #반복문 쓰지 않고 map,리스트,sum,zip적절히 이용하면 될 것 같다 생각했는데, 안될 듯
    for i in range(len(a)):
        answer+=a[i]*b[i]
    
    return answer