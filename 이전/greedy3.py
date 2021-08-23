import sys
N = int(sys.stdin.readline().rstrip())
ppl = list(map(int, sys.stdin.readline().rstrip().split()))
ppl.sort()
group = 0
gnum = 0
for i in ppl:
    gnum += 1
    if i <= gnum:
        gnum = 0
        group += 1
print(group)
