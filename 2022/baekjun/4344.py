testcase = int(input())
for t in range(testcase):
    scores = list(map(int,input().split()))
    avg_score = sum(scores[1:])/scores[0]
    cnt = 0
    for s in scores[1:]:
        if s > avg_score:
            cnt += 1

    print("{:.3f}%".format((cnt/scores[0])*100))