# https://programmers.co.kr/learn/courses/30/lessons/77884

# 제곱근(math.sqrt()) 써야하므로 math모듈 불러옴
import math

def solution(left, right):
    arr = []
    # left이상 right이하에서 for반복문
    for i in range(left, right+1):
        # 자연수의 약수가 홀수인경우는 자연수의 제곱밖에 없음
        # 제곱근의 버림과 제곱근이 같다면 자연수의 제곱이라는 뜻
        if int(math.sqrt(i)) == math.sqrt(i):
            # 이런경우는 빼기로 해준다
            arr.append(-i)
        else:
            # 제곱이 아닌경우는 더하기로 해준다
            arr.append(i)
    # sum은 어레이의 총합을 불러온다
    answer = sum(arr)
    return answer

# 어레이가 아니라 정수에다 바로 더하고 뺴도 된다

print(solution(13,17))

