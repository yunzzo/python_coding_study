import re
def solution(s):
    count = 0
    rm = 0
    while True:
        if s != "1":
            # 0 제거
            rm += s.count('0')
            s = re.sub(r'[0]+', '', s)
            # 이진변환
            s = format(len(s), 'b')
            count += 1
        elif s == "1":
            break
    
    result = [count, rm]
    return result
