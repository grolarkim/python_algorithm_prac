# def location (S, low, high):
#     if (low > high):
#         return 0
#     else:
#         mid = (low + high) // 2
#         if (x == S[mid]):
#             return mid
#         elif (x < S[mid]):
#             return location(S, low, mid - 1)
#         else:
#             return location(S, mid + 1, high)

# S = [-1, 10, 12, 13, 14, 18, 20, 25, 27, 30, 35, 40, 45]
# x = 18
# loc = location(S, 1, len(S) - 1)
# print('S =', S)
# print('x =', x)
# print('loc =', loc)


# def mergesort (S):
#     n = len(S)
#     if (n <= 1):
#         return S
#     else:
#         mid = n // 2
#         U = mergesort(S[0 : mid])
#         V = mergesort(S[mid : n])
#         return merge(U, V)

# def merge(U, V):
#     S = []
#     i = j = 0
#     while (i < len(U) and j < len(V)):
#         if (U[i] < V[j]):
#             S.append(U[i])
#             i += 1
#         else:
#             S.append(V[j])
#             j += 1
#     if (i < len(U)):
#         S += U[i : len(U)]
#     else:
#         S += V[j : len(V)]
#     return S

# S = [27, 10, 12, 20, 25, 13, 15, 22]
# print('Before: ', S)
# X = mergesort(S)
# print(' After: ', X)



def mergesort2 (S, low, high):
    if (low < high):
        mid = (low + high) // 2
        mergesort2(S, low, mid)
        mergesort2(S, mid + 1, high)
        merge2(S, low, mid, high)

def merge2 (S, low, mid, high):
    U = []
    i = low
    j = mid + 1
    while (i <= mid and j <= high):
        if (S[i] < S[j]):
            U.append(S[i])
            i += 1
        else:
            U.append(S[j])
            j += 1
    if (i <= mid):
        U += S[i : mid + 1]
    else:
        U += S[j : high + 1]
    for k in range(low, high + 1):
        S[k] = U[k - low]

S = [27, 10, 12, 20, 25, 13, 15, 22]
print('Before: ', S)
mergesort2(S, 0, len(S) - 1)
print(' After: ', S)

