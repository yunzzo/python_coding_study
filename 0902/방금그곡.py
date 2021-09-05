def solution(m, musicinfos):
    answer = ''
    answer_list = []
    index = 1
    for music in musicinfos:
        radio = ''
        info = music.split(',')
        start_time = list(map(int, info[0].split(':')))
        end_time = list(map(int, info[1].split(':')))
        space = end_time[1] - start_time[1]
        hour = (end_time[0] - start_time[0]) * 60
        real_space = space+hour
        cnt = 0
        while True:

            if len(radio) < real_space:
                radio += info[3][cnt]
                if cnt < len(info[3])-1:
                    if info[3][cnt+1] == '#':
                        radio += '#'
                        cnt += 2
                    else:
                        cnt += 1
                else:
                    cnt += 1
            else:
                break
            if cnt >= len(info[3]):
                cnt = 0
            if m in radio:
                compare_radio = radio + info[3][cnt]
                num = compare_radio.find(m)
                if compare_radio[num:num+len(m)+1] != m+'#':
                    answer_list.append((real_space, info[2], index))
                    break
                else:
                    break

        index += 1
    if len(answer_list) == 0:
        answer = "(None)"
    elif len(answer_list) == 1:
        answer = answer_list[0][1]
    else:
        answer_list = sorted(answer_list, key=lambda x: (-x[0], x[2]))
        answer = answer_list[0][1]
    print(answer_list)
    return answer


print(
    solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
