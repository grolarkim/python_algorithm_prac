a = int(input())

# a = 100001*b+10001*c+1001*d+101*e+11*f+2*g
aa = False
if a > 100:
    for i in range(a-100, a):
        b = (i//1000000)%10
        c = (i//100000)%10
        d = (i//10000)%10
        e = (i//1000)%10
        f = (i//100)%10
        g = (i//10)%10
        h = i%10
        if a == i+b+c+d+e+f+g+h:
            aa = True
            print(i)
            break
else:
    for i in range(a):
        f = (i//100)%10
        g = (i//10)%10
        h = i%10
        if a == i+f+g+h:
            aa = True
            print(i)
            break
if not aa:
    print(0)