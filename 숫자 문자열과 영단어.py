s = "one4seveneight"


def solution(s):
    answer_word = ''
    answer = ''
    for ele in s:
        if ele.isalpha():
            answer_word += ele
            if answer_word == 'zero':
                answer += '0'
                answer_word = ""
            elif answer_word == 'one':
                answer += '1'
                answer_word = ""
            elif answer_word == 'two':
                answer += '2'
                answer_word = ""
            elif answer_word == 'three':
                answer += '3'
                answer_word = ""
            elif answer_word == 'four':
                answer += '4'
                answer_word = ""
            elif answer_word == 'five':
                answer += '5'
                answer_word = ""
            elif answer_word == 'six':
                answer += '6'
                answer_word = ""
            elif answer_word == 'seven':
                answer += '7'
                answer_word = ""
            elif answer_word == 'eight':
                answer += '8'
                answer_word = ""
            elif answer_word == 'nine':
                answer += '9'
                answer_word = ""
        elif ele.isdigit():
            answer += str(ele)
    return int(answer)


print(solution(s))
