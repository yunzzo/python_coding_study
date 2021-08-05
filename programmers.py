num, base = map(int, input().strip().split(' '))
r = len(str(num))
answer = 0
for i in str(num):
    answer += int(i)*(base**(r-1))
    r -= 1

print(answer)

# 파이썬에서 int(x, base=10) 함수는 진법변환을 지원한다
# answer = int(num, base)
