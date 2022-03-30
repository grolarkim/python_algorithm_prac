# 10872
# def fac(a):
#     if a == 1 or a==0:
#         return 1
#     return a*fac(a-1)
# print(fac(int(input())))


# # 10870
# def fibo(a):
#     if a ==0:
#         return 0
#     elif a==1 or a==2:
#         return 1
#     else:
#         return fibo(a-1)+fibo(a-2)
# print(fibo(int(input())))


2447
def star(n):
    arr = making_star_arr(n)
    print_star(arr, n)


def print_star(arr, num):
    idx = 0
    while idx < len(arr):
        if idx%(num/3) == (num/3 - 1):
            print(arr[idx])
        else:
            print(arr[idx], end='')
        idx += 1

def making_star_arr(num):
    idx = 0
    result = []
    if num == 3:
        return ['***','* *','***']
    else:
        arr = making_star_arr(int(num/3))
        b = int(num/9)
        c = len(arr)
        while idx < num:
            if idx//int(num/3) == 1:
                for a in arr[(idx*b)%c:((idx*b)%c)+b]:
                    result.append(a)
                for j in range(b):
                    result.append('   ')
                for a in arr[(idx*b)%c:((idx*b)%c)+b]:
                    result.append(a)
            else:
                for j in range(3):
                    for a in arr[(idx*b)%c:((idx*b)%c)+b]:
                        result.append(a)
            idx += 1
        return result

star(int(input()))

arr3 = ['***','* *','***']
# arr9 = []

# for i in range(9):
#     if i//(9/3) == 1:
#         arr9.append(arr3[i%3])
#         arr9.append('   ')
#         arr9.append(arr3[i%3])
#     else:
#         for j in range(3):
#             arr9.append(arr3[i%3])

# print(len(arr9))
# print_star(arr9, 9)




# arr27= []
# num = 27
# idx = 0
# while idx < 27:
#     if idx//(num/3) == 1:
#         for a in arr9[idx*3%27:idx*3%27+int(num/9)]:
#             arr27.append(a)
#         for j in range(int(num/9)):
#             arr27.append('   ')
#         for a in arr9[idx*3%27:idx*3%27+int(num/9)]:
#             arr27.append(a)
#     else:
#         for j in range(3):
#             for a in arr9[idx*3%27:idx*3%27+int(num/9)]:
#                 arr27.append(a)
#     idx += 1

    
# print(arr27)
# print_star(arr27,27)

# for i in c:
#     print(i)




11729


# def hanoi(num):
#     print(hanoi_cnt(num))
#     hanoi_sub(num, 1, 2, 3)

# def hanoi_cnt(num):
#     if num == 1:
#         return 1
#     else:
#         return (hanoi_cnt(num-1)*2) + 1

# def hanoi_sub(num, a, b, c):
#     if num == 1:
#         print(a,c)
#     else:
#         hanoi_sub(num-1, a, c, b)
#         print(a,c)
#         hanoi_sub(num-1, b, a, c)

# hanoi(int(input()))



