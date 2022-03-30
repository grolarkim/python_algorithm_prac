from operator import itemgetter
import sys
testcase = int(sys.stdin.readline())
arr = []
for i in range(testcase):
    a = sys.stdin.readline().split()
    a = list(map(int, a))
    arr.append(a)
arr.sort(key= lambda x: (x[1], x[0]))
for b,c in arr:
    print(b,c)
