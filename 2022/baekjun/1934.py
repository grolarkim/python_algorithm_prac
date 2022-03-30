import sys
testcase = int(sys.stdin.readline())
for i in range(testcase):
    a,b = map(int, sys.stdin.readline().split())

    alist = []
    for i in range(1, a+1):
        if a%i == 0:
            alist.append(i)
    blist=[]
    for j in alist:
        if b%j == 0:
            blist.append(j)
    c = max(blist)

    print(a*b//c)