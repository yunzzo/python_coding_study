place = input()
col = ord(place[0]) - 96
row = int(place[1])

dx = [2, 1, -1, -1, -2, -2, -1, -1]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

ctn = 0
for i in range(8):
    nx = col + dx[i]
    ny = row + dy[i]
    if(nx < 9 and nx > 0 and ny < 9 and ny > 0):
        ctn += 1

print(ctn)
