def solution(arr1, arr2):
    rl = len(arr1)
    cl = len(arr1[0])
    answer = []
    for i in range(rl):
        row=[]
        for j in range(cl):
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
    return answer

print(solution())