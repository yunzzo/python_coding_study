import sys
N = int(sys.stdin.readline().rstrip())
plan = sys.stdin.readline().rstrip().split()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x = 1
y = 1
for i in range(N+1):
    diret = plan[i]
    if diret == 'R' and x < N:
        x += dx[1]
        y += dy[1]
    if diret == 'L' and x > 1:
        x += dx[3]
        y += dy[3]
    if diret == 'U' and y > 1:
        x += dx[2]
        y += dy[2]
    if diret == 'D' and y < N:
        x += dx[0]
        y += dy[0]

print(y, x)
