n = int(input())
plan = (input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
start_point = [1, 1]
previous_point = []
for i in plan:
    previous_point = start_point[:]
    if i == 'L':
        start_point[0] += dx[0]
        start_point[1] += dx[0]
    if i == 'R':
        start_point[0] += dx[1]
        start_point[1] += dy[1]
    if i == 'U':
        start_point[0] += dx[2]
        start_point[1] += dy[2]
    if i == 'D':
        start_point[0] += dx[3]
        start_point[1] += dy[3]
    print(start_point[0], start_point[1], previous_point[0], previous_point[1])
    if start_point[0] < 1 or start_point[0] > n or start_point[1] < 1 or start_point[1] > n:  # 범위를 벗어났을 경우
        start_point = previous_point  # 연산결과(이동한 결과) 상쇄시켜 줌

# 출력
print(start_point[0], start_point[1])
