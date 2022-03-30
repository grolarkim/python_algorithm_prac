testcase = int(input())
testlist = list(map(int, input().split()))
sorted_list = sorted(testlist)
print(sorted_list[0]*sorted_list[-1])