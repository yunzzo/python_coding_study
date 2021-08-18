#프로그래머스 레벨1 숫자 문자열과 영단어
"""
number_alpha설정하는 과정,
number=list(map(str,[x for x in range(10)]))
alpha=['zero','one','two','three','four','five','six','seven','eight','nine']
후
number_alpha=list(zip(number,alpha))해도 될 듯
근데 이렇게하면 리스트안에 튜플 형식으로 된다.

"""
def solution(s):
    answer = 0
    number_alpha=[["0","zero"],["1","one"],["2","two"],["3","three"],["4","four"],["5","five"],["6","six"],["7","seven"],["8","eight"],["9","nine"]]
    #사실 위에것 zip함수 활용해서 더 쉽게 만들어줄 수 있긴 함
    if not (s.isdigit()):
        for i in number_alpha:
            #영어를 숫자로 바꾸는 과정
            #replace함수는 새 객체를 반환하니까, 변수에 넣어줘야지! 원본을 변경시키는게 아님
            s=s.replace(i[1],i[0])
    
    answer=int(s)
    print(answer)
    return answer