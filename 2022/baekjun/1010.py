import sys
from math import factorial
testcase = int(sys.stdin.readline())
for i in range(testcase):
    b,a = map(int, sys.stdin.readline().split())
    print(int(factorial(a)/(factorial(b)*factorial(a-b))))