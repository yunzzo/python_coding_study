def solution(nums):
    answer = 0
    len_nums=len(nums)
    set_nums=set(nums)
    #가져갈 수 있는 포켓몬 >= 중복제거한 포켓몬 수 일 때
    if len_nums/2 >= len(set_nums):
        #그냥 중복제거한 포켓몬 길이가 정답
        answer=len(set_nums)
    #중복제거한 포켓몬 수가 더 많다면
    else:
        #가져갈 수 있는 포켓몬 수가 정답
        answer=len_nums/2
    return answer