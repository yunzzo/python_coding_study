x= 3
a=4

def mysqrt(a,x):
    while True:
        print(x)
        y = (x+a/x) /2
        if abs(y-x)<1e-15:
            break
        x =y

    return y

mysqrt(4,10)
for a in range(1,1000):
    print('----',a,'----')
    mysqrt(a,a)