import sys

N, K = map(int, sys.stdin.readline().split())
ctn = 0
while(1):
    if(N == 1):
        break
    if(N % K == 0):
        ctn += 1
        N //= K
    else:
        while(1):
            if(N == 1):
                break
            if(N % K == 0):
                break
            else:
                ctn += 1
                N -= 1

print(ctn)
