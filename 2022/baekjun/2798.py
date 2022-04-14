import itertools


a,b = map(int, input().split())
list1 = list(map(int, input().split()))
c = map(sum, itertools.combinations(list1, 3))
d = [x for x in c if x <= b]
print(max(d))