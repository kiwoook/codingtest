import math


def is_prime(x):
    for u in range(2, int(math.sqrt(x) + 1)):
        if x % u == 0:
            return False
    return True


m, n = map(int, input().split())

for i in range(m, n + 1):
    if i == 1:
        continue
    if is_prime(i):
        print(i)
