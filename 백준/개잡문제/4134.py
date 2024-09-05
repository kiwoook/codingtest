import math
import sys


def is_prime(value):
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            return False

    return True


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    num = int(sys.stdin.readline().rstrip())

    while num <= 1 or not is_prime(num):
        num += 1

    print(num)
