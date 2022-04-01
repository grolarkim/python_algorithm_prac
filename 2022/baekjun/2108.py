from collections import Counter
import sys

testcase = int(sys.stdin.readline())
num_list = []
for i in range(testcase):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()
print(round(sum(num_list)/testcase))
print(num_list[testcase//2])
cnt = Counter(num_list).most_common()
if len(cnt) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(num_list[-1]-num_list[0])