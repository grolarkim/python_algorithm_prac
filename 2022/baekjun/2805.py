import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
mi = 1
ma = max(arr)
while mi <= ma:
    a = (mi+ma)//2
    total = [i-a if i>a else 0 for i in arr]
    mm = sum(total)
    if mm > M:
        mi = a + 1
    elif mm < M:
        ma = a - 1
    else:
        ma = a
        break
print(ma)