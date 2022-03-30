a = input()
idx = 0
cnt = 0 
while idx < len(a):
    if a[idx:idx+2]=='c=':
        idx += 2
        cnt += 1
    elif a[idx:idx+2]=='c-':
        idx += 2
        cnt += 1
    elif a[idx:idx+3]=='dz=':
        idx += 3
        cnt += 1
    elif a[idx:idx+2]=='d-':
        idx += 2
        cnt += 1
    elif a[idx:idx+2]=='lj':
        idx += 2
        cnt += 1
    elif a[idx:idx+2]=='nj':
        idx += 2
        cnt += 1
    elif a[idx:idx+2]=='s=':
        idx += 2
        cnt += 1
    elif a[idx:idx+2]=='z=':
        idx += 2
        cnt += 1
    else:
        idx += 1
        cnt += 1
print(cnt)