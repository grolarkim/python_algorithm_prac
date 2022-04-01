import sys

testcase = int(sys.stdin.readline())
a_list = []
num_list = [i for i in range(1,testcase+1)]
for i in range(testcase):
    a_list.append(int(sys.stdin.readline()))

print(a_list)