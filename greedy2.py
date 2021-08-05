import sys
num = sys.stdin.readline().rstrip()
result = int(num[0])
for i in range(1, len(num)):
    n = int(num[i])
    if(result <= 1 or n <= 1):
        result += int(n)
        print(result)
    else:
        result *= n
        print(result)

print(result)
