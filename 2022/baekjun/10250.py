testcase = int(input())
for i in range(testcase):
    a,b,c = map(int, input().split())
    d = c//a
    e = c%a

    if e == 0:
        print(a*100+d)
    else:
        print(e*100+d+1)