import sys


testcase = int(input())
for t in range(testcase):
    x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        dsq = ((x1-x2)**2)+((y1-y2)**2)
        if (r1+r2)**2 == dsq:
            print(1)
        elif (r1-r2)**2 == dsq:
            print(1)
        elif dsq > (r1+r2)**2:
            print(0)
        elif dsq < (r1-r2)**2:
            print(0)
        else:
            print(2)
