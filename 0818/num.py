def solution(s):
    answer =[]
    i=0
    while (i < len(s)):
        if s[i].isalpha():
            if s[i] == 'z':
                answer.append(0)
                i += 4
                continue

            if s[i] == 'o':
                answer.append(1)
                i += 3
                continue

            if s[i] == 't':
                if s[i+1] == 'w':
                    answer.append(2)
                    i += 3
                    continue

                elif s[i+1] == 'h':
                    answer.append(3)
                    i+=5
                    continue

            if s[i] == 'f':
                if s[i+1] == 'o':
                    answer.append(4)
                    i +=4
                    continue
                else:
                    answer.append(5)
                    i+=4
                    continue

            if s[i] == 's':
                if s[i+1] == 'i':
                    answer.append(6)
                    i+=3
                    continue

                else:
                    answer.append(7)
                    i+=5
                    continue

            if s[i] == 'e':
                answer.append(8)
                i+= 5
                continue

            if s[i] == 'n':
                answer.append(9)
                i+= 4
                continue

        elif s[i].isdigit():
            answer.append(s[i])
            i += 1
            continue

    answer = ''.join(map(str, answer))
    return int(answer)


print(solution("56two"))


