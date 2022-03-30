# 10952
# while True:
#     array = input().split()
#     a = int(array[0])
#     b = int(array[1])
    
#     if a == 0:
#         break
#     print(a+b)


# # 10951
# while True:
#     try:
#         a,b = map(int, input().split())
#         print(a+b)
#     except:
#         break

# import sys
# input_cases = sys.stdin.readlines()
# for case in input_cases:
#     a, b = map(int, case.split())
#     print(a+b)

# while case := sys.stdin.readline():
#     a, b = map(int, case.split())
#     print(a+b)


# # 1110
firstN = int(input())
N = firstN
count1 = 0
while True:
    a = N//10
    b = N%10
    c = (a+b)%10
    N = (b*10) + c
    count1 += 1
    if N == firstN:
        break
print(count1)
# ##########################

firstN = int(input())
N = firstN
cycle=0
while 1:

    a = N // 10
    b = N % 10
    c = a + b
    d = (b * 10) + (c % 10)
    cycle += 1
    if d == firstN:
        print(cycle)
        break
    else:
        N = d
        print(N)

############################


init_num = int(input())
init_changeable_num = init_num
round = 0
while True:
    round += 1
    if init_changeable_num < 10:
        next_num = init_changeable_num*10 + init_changeable_num
    else:
        r_num = init_changeable_num%10
        out_num = init_changeable_num//10 + r_num
        next_num = r_num*10 + out_num%10
    if (init_num == next_num): break
    init_changeable_num = next_num
print(round)

