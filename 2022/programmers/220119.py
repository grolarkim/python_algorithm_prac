# https://programmers.co.kr/learn/courses/30/lessons/64061

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	
moves = [1,5,3,5,1,2,1,4]
result = 4
# print(len(board))

def solution1(board, moves):
    stack = []
    count = 0
    n = len(board)

    
    # 뽑기 반복
    for move in moves:
        for i in range(n):
            # 뽑을게 남아있으면
            if board[i][move-1] != 0:
                # 뽑아서 스택에 넣기
                stack.append(board[i][move-1])
                # print(stack)
                # 뽑은 자리 공백으로
                board[i][move-1] = 0
                
                # 스택의 길이가 2이상에 마지막 2개가 같다면
                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        # 마지막 2인형 제거후 카운트
                        stack.pop()
                        stack.pop()
                        count += 2
                break

    # print(stack)
    return count

print(solution1(board, moves))

# https://programmers.co.kr/learn/courses/30/lessons/70128

a1, b1 = [1,2,3,4],	[-3,-1,0,2]
a2, b2 = [-1,0,1],	[1,0,-1]

def solution2(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

print(solution2(a1,b1))
print(solution2(a2,b2))

# https://programmers.co.kr/learn/courses/30/lessons/81301

s = "one4seveneight"

def solution3(s):
    chars = ['zero','one','two','three','four','five','six','seven','eight','nine']
    ans = ''

    while len(s) > 0:
        if s[0].isdecimal():
            ans = ans + s[0]
            s = s[1:]
        else:
            for i in range(10):
                c = chars[i]
                d = len(c)
                if s[:d] == c:
                    ans = ans + str(i)
                    s = s[d:]
                    break

    return int(ans)