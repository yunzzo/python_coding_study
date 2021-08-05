s, n = input().strip().split(' ')
n = int(n)
print(s, ' '*(n-len(s)-1))
r = (n-len(s))//2
print(' '*(r-1), s, ' '*(r-1))
print(' '*(n-len(s)-1), s)

# s.ljust(n) 촤측정렬
# s.center(n) 가운데 정렬
# s.rjust(n) 우측정렬
