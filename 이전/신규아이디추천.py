new_id = "=.="


def solution(new_id):
    new_id = new_id.lower()
    answer = ''
    for i in new_id:
        if i not in '~!@#$%^&*()=+[{]}:?,<>/':
            answer += i
    new_id = ''
    cnt = 0
    for i in answer:
        if i == '.':
            cnt += 1
            if cnt < 2:
                new_id += i
        else:
            cnt = 0
            new_id += i

    if new_id[0] == '.':
        new_id = new_id[1:]

    if len(new_id) >= 1:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if new_id == '':
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[0:15]

        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) <= 2:
        i = new_id[-1]

        while True:
            new_id += i
            if len(new_id) == 3:
                break

    return new_id


print(solution(new_id))
