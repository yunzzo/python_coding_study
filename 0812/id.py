def solution(new_id):
    #1
    new_id = new_id.lower()
    #2
    trash = '~!@#$%^&*()=+[{]}:?,<>/'
    new_id = ''.join(x for x in new_id if x not in trash)
    #3
    i = 0
    while(i<(len(new_id)-1)):
        if new_id[i] == '.':
            if new_id[i+1] == '.':
                new_id = new_id[:i] + new_id[i+1:]
            else:
                i += 1
        else:
            i += 1
    #4
    if len(new_id) != 1:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    else:
        if new_id == '.':
            new_id = ''
    #5
    if len(new_id) == 0:
        new_id = 'a'
    #6
    if len(new_id) >=16:
        if new_id[14] == '.':
            new_id = new_id[:14]
        else:
            new_id = new_id[:15]
    #7
    if len(new_id) <= 2:
        while(len(new_id) < 3):
            new_id += new_id[-1]
    answer = new_id
    return answer

print(solution("abcdefghijklmn.p"))

