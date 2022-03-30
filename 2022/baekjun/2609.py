a,b = map(int, input().split())

alist = []
for i in range(1, a+1):
    if a%i == 0:
        alist.append(i)
blist=[]
for j in alist:
    if b%j == 0:
        blist.append(j)
c = max(blist)
print(c)
print(a*b//c)