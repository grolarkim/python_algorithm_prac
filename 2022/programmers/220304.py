n =	5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        ans_str = ""
        x,y = str(format(arr1[i], 'b')), str(format(arr2[i], 'b')) 
        x,y = x.rjust(n,"0"), y.rjust(n,"0")
        for j in range(n):
            if x[j] == "0" and y[j] == "0":
                ans_str = ans_str + " "
            else:
                ans_str = ans_str + "#"
        answer.append(ans_str)
    return answer

answer = []


print(answer)
