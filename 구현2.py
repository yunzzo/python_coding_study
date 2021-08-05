import sys
N = int(sys.stdin.readline())
ctn = 0
for i in range(N+1):
    for k in range(60):
        for j in range(60):
            if '3' in str(j) + str(k) + str(i):
                ctn += 1

print(ctn)
