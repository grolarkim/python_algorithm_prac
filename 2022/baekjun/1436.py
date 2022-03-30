a = int(input())
index = 0
cnt = 0
while True:
    index += 1
    if "666" in str(index):
        cnt+=1
    if cnt == a:
        print(index)
        break
