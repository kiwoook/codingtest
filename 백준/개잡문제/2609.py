import math

a, b = map(int, input().split())
gcd = math.gcd(a,b)

print(gcd)
print(gcd * (a // gcd) * (b // gcd))