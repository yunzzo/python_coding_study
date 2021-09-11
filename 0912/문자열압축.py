def solution(s):
    answer = ""
    result = 10000
    for i in range(1, len(s)+1):
        prev = ""
        count = 1
        for ele in range(0, len(s), i):
            now = s[ele:ele+i]

            if prev != "":
                if prev == now:
                    count += 1
                else:
                    if count != 1:
                        answer += str(count) + prev
                        count = 1
                    else:
                        answer += prev
            prev = now
        if count != 1:
            answer += str(count) + prev
            count = 1
        else:
            answer += prev
        if result > len(answer):
            result = len(answer)
        answer = ""

    return result


print(solution("aabbaccc"))
