testcase = int(input())

for t in range(testcase):
    a,b = list(map(int,input().split()))
    c = b-a
    d = int(c**0.5) 
    if d**2 == c:
        print(2*d-1)
    elif (d*d + d) < c:
        print(2*d+1)
    else:
        print(2*d)
