def is_prime(i):
    if i == 1:
        return False
    elif i==2 or i==3:
        return True
    for j in range(2,int(i**0.5)+2):
        if i%j == 0:
            return False
    return True

a,b = map(int, input().split())
for i in range(a,b+1):
    if is_prime(i):
        print(i)