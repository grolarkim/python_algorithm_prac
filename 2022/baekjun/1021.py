len_list, cnt = map(int, input().split())
list1 = list(map(int, input().split()))
num_list = [i for i in range(1,len_list+1)]
cur_q = 0
cnt = 0
for i in list1:
    idx = num_list.index(i)
    l = len(num_list)
    a = idx - cur_q
    if a > 0:
        if l-a > a:
            cnt += a
        else:
            cnt += l-a
    else:
        if l+a > -a:
            cnt -= a
        else:
            cnt += l+a
    # print(cnt)
    cur_q = idx
    num_list.remove(i)
    # print(num_list)
print(cnt)