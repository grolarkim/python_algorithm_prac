n,computers = 3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def solution(n, computers):
    global network 
    network = []
    answer = 0
    for i in range(n):
        if i not in network:
            answer +=1
            search(i, computers)
    return answer

network = []
for i in range(n):
    if i not in network:
        network.append(i)
        for idx,j in enumerate(computers[i]):
            if j == 1 and idx not in network:
                network.append(idx)
    else:
        print(i)


def search(x,computers):
    if x not in network:
        network.append(x)
        for idx, j in enumerate(computers[x]):
            if j == 1 and idx not in network:
                search(idx, computers)
    
