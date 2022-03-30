def hanoi(num):
    print(hanoi_cnt(num))
    hanoi_sub(num, 1, 2, 3)

def hanoi_cnt(num):
    if num == 1:
        return 1
    else:
        return (hanoi_cnt(num-1)*2) + 1

def hanoi_sub(num, a, b, c):
    if num == 1:
        print(a,c)
    else:
        hanoi_sub(num-1, a, c, b)
        print(a,c)
        hanoi_sub(num-1, b, a, c)

hanoi(int(input()))