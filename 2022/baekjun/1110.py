a = int(input())
cnt = 0
a_copy = a
while True:
    cnt += 1
    b=a//10
    c=a%10
    a = (c*10)+((b+c)%10)
    if a == a_copy:
        break

print(cnt)