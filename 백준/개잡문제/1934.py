import math
import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    gcd = math.gcd(a, b)
    print(a * b // gcd)
