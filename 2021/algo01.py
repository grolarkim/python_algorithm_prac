
# 질문방문제
n = [45, 73, 66, 87, 92, 67, 75, 79, 75, 80]
k = sum(n)/len(n)

absarray = [abs(x-k) for x in n] #평균 값과의 차이로 만든 배열
min_index = absarray.index(min(absarray)) #배열의 최솟값의 인덱스를 구함

print(n[min_index])
