import sys
from collections import deque
testcase = int(sys.stdin.readline())
arr = deque()
for i in range(testcase):
    a = int(sys.stdin.readline().split()[0])
    if a == 0:
        arr.pop()
    else:
        arr.append(a)
print(sum(arr))