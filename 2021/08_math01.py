# 1712 'BREAK-EVEN POINT'
# 수학을 해야함 하나씩 더하면 시간초과

# a,b,c = 1000, 70, 170
# a,b,c = 3,2,1

# a,b,c = map(int,input().split())
# if b >= c:
#     print(-1)
# else:
#     idx = int(a/(c-b))
#     print(idx+1)


# 2869
# a,b,v = 2, 1, 5
# a,b,v = 5, 1, 6
# a,b,v = 100, 99, 1000000000

# import math
# a,b,v = map(int,input().split())
# x = math.ceil((v-a)/(a-b))
# print(x+1)

# ##########################

# import math

# a, b, v = map(int, input().split())
# day = math.ceil((v-b) / (a-b))
# print(day)


1011
import math
T = int(input())
for i in range(T):
    x,y = map(int,input().split())
    space = (y-x)

    z = int(math.sqrt(space))

    if space > z*(z+1):
        time = 2*z + 1
    elif space == z**2:
        time = 2*z -1
    else:
        time = 2*z
        
    print(time)


##############
t = int(input())

for _ in range(t):
    x, y = map(int,input().split())
    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance :
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0 :  # count가 2의 배수일 때,
            move += 1
    print(count)

1
1
11
2
121
4
1221
6
12321
9 3*3
123321
12 3*4
1234321 4
16 4*4
12344321 8
20 4*5
123454321 9
25 5*5
