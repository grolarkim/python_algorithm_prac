import sys
from math import factorial
a,b = map(int, sys.stdin.readline().split())

print(int(factorial(a)/(factorial(b)*factorial(a-b))))