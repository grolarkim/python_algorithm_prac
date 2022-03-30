# def binsearch(n, S, x):
#     low = 1
#     high = n
#     location = 0
#     while (low <= high and location == 0):
#         mid = (low + high) // 2
#         # print(low, mid, high)
#         if (x == S[mid]):
#             location = mid
#         elif (x < S[mid]):
#             high = mid - 1
#         else:
#             low = mid + 1
#     return location

# S = [-1, 5, 7, 8, 10, 11, 13]
# # x = 2
# x = 7
# # x = 13
# location = binsearch(len(S) - 1, S, x)
# print('S =', S)
# print('x =', x)
# print('location =', location)


# def fib (n):
#     if (n <= 1):
#         return n
#     else:
#         return fib(n - 1) + fib(n - 2)

# for i in range(11):
#     print(fib(i), end=" ")

def fib2 (n):
    f = [0] * (n + 1)
    if (n > 0):
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
    return f[n]
for i in range(100):
    print(fib2(i), end=" ")

