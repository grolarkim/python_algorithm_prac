import sys


N = int(sys.stdin.readline())
paper = []
for i in range(N):
    paper.append(list(map(int,sys.stdin.readline().split())))

print(paper)