numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"


def solution(numbers, hand):
    answer = ''
    L = (1, 4)
    R = (3, 4)
    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            left = numbers[i]
            answer += 'L'
            if left == 1:
                L = (1, 1)
            elif left == 4:
                L = (1, 2)
            elif left == 7:
                L = (1, 3)
        elif numbers[i] in [3, 6, 9]:
            right = numbers[i]
            answer += 'R'
            if right == 3:
                R = (3, 1)
            elif right == 6:
                R = (3, 2)
            elif right == 9:
                R = (3, 3)
        else:
            E = numbers[i]
            if E == 2:
                E = (2, 1)
            elif E == 5:
                E = (2, 2)
            elif E == 8:
                E = (2, 3)
            elif E == 0:
                E = (2, 4)
            if(abs(E[0]-L[0])+abs(E[1]-L[1]) > abs(E[0]-R[0])+abs(E[1]-R[1])):
                answer += 'R'
                R = E
            elif(abs(E[0]-L[0])+abs(E[1]-L[1]) < abs(E[0]-R[0])+abs(E[1]-R[1])):
                answer += 'L'
                L = E
            elif(abs(E[0]-L[0])+abs(E[1]-L[1]) == abs(E[0]-R[0])+abs(E[1]-R[1])):
                if hand == 'right':
                    answer += 'R'
                    R = E
                elif hand == 'left':
                    answer += 'L'
                    L = E

    return answer


print(solution(numbers, hand))
