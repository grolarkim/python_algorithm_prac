# def seqsearch (n, S, x):
#     location = 1
#     while (location <= n and S[location] != x):
#         location += 1
#     if (location > n):
#         location = 0
#     return location

# S = [0, 10, 7, 11, 5, 13, 8]
# x = 4
# location = seqsearch(len(S) - 1, S, x)
# print('location =', location)



# list1 = [-1, 10, 7, 11, 5, 13, 8]

# def sum(n, S):
#     a = 0
#     for i in range(1, n+1):
#         a = a + S[i]
#     return a

# sum(len(list1)-1, list1)
# print(len(list1))
# print(sum(len(list1)-1, list1))




# a = [-1, 10, 7, 11, 5, 13, 8]

# def exchange(S):
#     n = len(S)
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if (S[i] > S[j]):
#                 S[i], S[j] = S[j], S[i]
#         print(S)

# print(a)
# exchange(a)
# print(a)


def matrixmult (A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[2, 3], [4, 1]]
B = [[5, 7], [6, 8]]
print('A =', A)
print('B =', B)
C = matrixmult(A, B)
print('C =', C)