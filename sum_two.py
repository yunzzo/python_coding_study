#프로그래머스 레벨1 두 개 뽑아서 더하기
"""
range(5,5)는 뭐지?
아무것도 없는건가?
인덱스 에러 발생안한거 보면 그런 것 같은데
range(시작값,종료값)에서, 시작값=종료값일 때

"""
def solution(numbers):
    answer = []
    #전부 배열에 담고 나서, set으로 중복 제거하고, 다시 리스트로 만든 후 오름차순으로 정렬(sort나 sorted함수 사용)
    #그냥 반복문으로, 한번씩 다 더해보면 됨(모든 경우의 수 충족)
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            print(j)
            answer.append(numbers[i]+numbers[j])
    
    
    #set으로 중복 제거
    answer=set(answer)
    answer=list(answer)
    answer.sort()
    return answer