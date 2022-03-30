
def solution(rows, columns, queries):
    answer = []
    origin_matrix = []
    for i in range(rows):
        origin_matrix.append(list(j+1+i*columns for j in range(columns)))
    # for q in queries:
    for q in queries:
        rowmin, colmin, rowmax, colmax = list(map(lambda x: x-1,q))
        intmin = rows*columns

        for i in range(rowmin, rowmax):
            origin_matrix[i][colmin] = origin_matrix[i+1][colmin]
            if origin_matrix[i+1][colmin] < intmin:
                intmin = origin_matrix[i+1][colmin]  
        for i in range(colmin, colmax):
            origin_matrix[rowmax][i] = origin_matrix[rowmax][i+1]
            if origin_matrix[rowmax][i+1] < intmin:
                intmin = origin_matrix[rowmax][i+1]
        for i in range(rowmin+1, rowmax+1):
            origin_matrix[i][colmax] = origin_matrix[i-1][colmax]
            if origin_matrix[i-1][colmax] < intmin:
                intmin = origin_matrix[i-1][colmax]
        for i in range(colmin+1, colmax+1):
            origin_matrix[rowmin][i] = origin_matrix[rowmin][i-1]
            if origin_matrix[rowmin][i-1] < intmin:
                intmin = origin_matrix[rowmin][i-1]
        
        answer.append(intmin)
    return answer

def solution(rows, columns, queries):
    answer = []
    table = []
    for r in range(rows):
        table.append([a for a in range(r*columns+1, (r+1)*columns+1)])
    
    for query in queries:
        query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = table[query[0]][query[1]] # 왼쪽 위 값 저장
        small = tmp
        
        # left
        for i in range(query[0]+1, query[2]+1):
            table[i-1][query[1]] = table[i][query[1]]
            small = min(small, table[i][query[1]])
        # bottom
        for i in range(query[1]+1, query[3]+1):
            table[query[2]][i-1] = table[query[2]][i]
            small = min(small, table[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            table[i+1][query[3]] = table[i][query[3]]
            small = min(small, table[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            table[query[0]][i+1] = table[query[0]][i]
            small = min(small, table[query[0]][i])
        table[query[0]][query[1]+1] = tmp
        
        answer.append(small)
    
    return answer



# rows,columns,queries = 6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]
# answer = []
# origin_matrix = []
# for i in range(rows):
#     origin_matrix.append(list(j+1+i*columns for j in range(columns)))
# # next_matrix = deepcopy(origin_matrix)
# # for q in queries:
# for q in queries:
#     rowmin, colmin, rowmax, colmax = list(map(lambda x: x-1,q))
#     intmin = rows*columns

#     for i in range(colmin+1, colmax+1):
#         next_matrix[rowmin][i] = origin_matrix[rowmin][i-1]
#         intmin = min(intmin, next_matrix[rowmin][i])
#     for i in range(rowmin+1, rowmax+1):
#         next_matrix[i][colmax] = origin_matrix[i-1][colmax]
#         intmin = min(intmin, next_matrix[i][colmax])
#     for i in range(colmin, colmax):
#         next_matrix[rowmax][i] = origin_matrix[rowmax][i+1]
#         intmin = min(intmin, next_matrix[rowmax][i])
#     for i in range(rowmin, rowmax):
#         next_matrix[i][colmin] = origin_matrix[i+1][colmin]
#         intmin = min(intmin, next_matrix[i][colmin])    
#     answer.append(intmin)
#     origin_matrix = deepcopy(next_matrix)

# print(answer)