testcase = int(input())
cnt = 0
for i in range(testcase):
    a = list(input())
    clist = [a[0]]
    if len(a) == 1:
        cnt+=1
    for i in range(1,len(a)):
        if a[i-1] == a[i]:
            pass
        elif a[i] in clist:
            break
        else:
            clist.append(a[i-1])
        if i == len(a)-1:
            cnt += 1
print(cnt)
