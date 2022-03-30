import sys
from collections import deque
testcase = int(sys.stdin.readline())
arr = deque()
for i in range(testcase):
    a = sys.stdin.readline().split()
    if a[0] == "top":
        if arr:
            print(arr[-1])
        else:
            print(-1)
    elif a[0] == "pop":
        if arr:
            print(arr.pop())
        else:
            print(-1)
    elif a[0] == "size":
        print(len(arr))
    elif a[0] == "empty":
        if arr:
            print(0)
        else:
            print(1)
    elif "push" in a:
        x = a[1]
        arr.append(int(x))