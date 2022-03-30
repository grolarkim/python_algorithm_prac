h,m = list(map(int,input().split()))
a = (h*60+m)-45
if a < 0:
    a += 1440
print(a//60, a%60)