
# 10818
# N = int(input())
# arr = [int(x) for x in input().split()]
# maxa = arr[0]
# mina = arr[0]
# for a in arr:
#     if a > maxa:
#         maxa = a
# for b in arr:
#     if b < mina:
#         mina = b
# print(mina, maxa)

# ###########

# N = int(input())
# arr = list(map(int,input().split()))
# print(min(arr), max(arr))



# 2577
# A = int(input())
# B = int(input())
# C = int(input())
# D = str(A*B*C)
# for i in range(10):
#     print(D.count(str(i)))

# 3052
# arr = []
# for _ in range(10):
#     arr.append(int(input())%42)
# arrset = set(arr)
# print(len(arrset))

# 1546
# testcase = int(input())
# scores = list(map(int, input().split()))
# maxscore = max(scores)
# b_scores = list(map((lambda x: x/maxscore*100),scores))
# aver = sum(b_scores)/len(b_scores)
# print(aver)

# 2562
# arr = []
# for _ in range(9):
#     arr.append(int(input()))
# maxarr = max(arr)
# indarr = arr.index(maxarr)
# print(maxarr)
# print(indarr+1)

# 4344
test_case = int(input())
for _ in range(test_case):
    scores = list(map(int, input().split()))
    aver = (sum(scores)-scores[0])/scores[0]
    over_count = 0
    for score in scores[1:]:
        if score > aver:
            over_count += 1
    result = (over_count/scores[0])*100
    print('{:.3f}%'.format(result))


############################################
C = int(input())
for i in range(C):
    N = list(map(int, input().split(' ')))
    avg = sum(N[1:]) / N[0]
    cnt = 0
    for k in N[1:]:
        if k > avg:
            cnt += 1

    print(str("%.3f" % round((cnt / N[0]) * 100, 3)) + "%")

################################

C=int(input())

for i in range(C):
    score=list(map(int, input().split()))
    # print(score)
    avg=(sum(score)-score[0])/score[0]
    students =[]
    for j in score:
        if j > avg:
            students.append(j)
    print('{:.3f}%'.format(round(len(students)/score[0]*100, 3)))
