from itertools import combinations


N,M = map(int, input().split())
a = list(combinations([i for i in range(1, N+1)],M))
for i in a:
    for j in i:
        print(j, end=" ")
    print()