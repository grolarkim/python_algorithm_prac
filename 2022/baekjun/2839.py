a = int(input())

remainderdict = [0,1,2,1,2,1,2,3,2,3,2,3,4,3,4]
minuslist=[4,7]
if a in minuslist:
    print("-1")
else:
    b = a//15
    c = a%15
    print(b*3+remainderdict[c])