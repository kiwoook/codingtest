import math
import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
c, d = map(int, sys.stdin.readline().rstrip().split())

e = a * d + c * b
f = b * d

g = math.gcd(e, f)
print(e // g, f // g)
