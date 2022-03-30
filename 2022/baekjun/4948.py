def is_prime(i):
    if i == 1:
        return False
    elif i==2 or i==3:
        return True
    for j in range(2,int(i**0.5)+2):
        if i%j == 0:
            return False
    return True

prime_list = []
for i in range(1,250000):
    if is_prime(i):
        prime_list.append(i)

while True:
    a = int(input())
    if a==0:
        break
    cnt = 0
    min_prime = 0
    max_prime = 0
    for i in range(a+1, 2*a+1):
        if i in prime_list:
            min_prime = i
            break
    for i in range(2*a, a, -1):
        if i in prime_list:
            max_prime = i
            break
    b = prime_list.index(max_prime)-prime_list.index(min_prime)

    print(b+1)