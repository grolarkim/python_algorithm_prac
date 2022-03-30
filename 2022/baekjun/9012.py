import sys
testcase = int(sys.stdin.readline())
for i in range(testcase):
    a = list(sys.stdin.readline())
    cnt = 0
    for p in a:
        if p == "(":
            cnt += 1
        elif p == ")":
            cnt -= 1
        if cnt < 0:
            break
    if cnt == 0:
        print("YES")
    else:
        print("NO")