# 2581
# import time
# start = time.time()
# M = int(input())
# N = int(input())
# arr = []

# for a in range(M,N+1):
#     cnt = 0
#     for x in range(1,a+1):
#         if a%x == 0:
#             cnt+=1
#             if cnt > 2:
#                 break
#     if cnt == 2:
#         arr.append(a)

# if arr:
#     print(sum(arr))
#     print(arr[0])
# else:
#     print(-1)
# end = time.time()
# print(f"{end - start:.5f} sec")


######################################

# m=int(input())
# n=int(input())

# ans = []
# bns=[]

# for i in range(m, n+1):
#     bns.append(i)
#     for j in range(2, i):
#         if i % j==0:
#             ans.append(i)
#             break

# for k in ans:
#     if k in bns:
#         bns.remove(k)
#     if 1 in bns:
#         bns.remove(1)


# if len(bns)==0:
#     print(-1)

# else:
#     print(sum(bns))
#     print(min(bns))



# # 1929
# import time
# start = time.time()
# import math
# M,N = map(int, input().split())
# def b(a):
#     if a == 1:
#         return False
#     else:
#         for x in range(2,int(math.sqrt(a))+1):
#             if a%x == 0:
#                 return False
#         return True

# for a in range(M,N+1):
#     if b(a):
#         print(a)
# end = time.time()
# print(f"{end - start:.5f} sec")


# 1002
# 문제를 잘읽자

T = int(input())
for i in range(T):
    X1, Y1, R1, X2, Y2, R2 = map(int, input().split())
    if X1==X2 and Y1==Y2 and R1 == R2:
        print(-1)
    elif (X1-X2)**2 + (Y1-Y2)**2 == (R1+R2)**2 or (X1-X2)**2 + (Y1-Y2)**2 == (R1-R2)**2:
        print(1)
    elif (X1-X2)**2 + (Y1-Y2)**2 > (R1+R2)**2:
        print(0)
    elif (X1-X2)**2 + (Y1-Y2)**2 < (R1-R2)**2:
        print(0)
    else:
        print(2)


# 1085
# x,y,w,h = map(int, input().split())
# arr=[x,y,w-x,h-y]
# print(min(arr))





