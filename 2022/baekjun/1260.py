from collections import deque
import sys


N,M,V = map(int, sys.stdin.readline().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(M):
    a,b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1


def dfs(V):
    visited = []
    queue = deque()
    queue.append(V)
    while queue: 
        a = queue.pop()
        # print(a, end=" ") 
        for i in range(N, 0, -1):
            if (i not in visited) and graph[a][i] == 1:
                queue.append(i) 
                visited.append(i)
    return visited



def bfs(V):
    visited = [V]
    queue = deque()
    queue.append(V)
    while queue: 
        a = queue.popleft()
        # print(a, end=" ") 
        for i in range(1, N+1): 
            if i not in visited and graph[a][i] == 1:
                queue.append(i) 
                visited.append(i)
    return visited



print(*dfs(V))
print()
print(*bfs(V))
