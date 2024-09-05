import math
import sys


def is_prime(value):
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True


s = sys.stdin.readline().rstrip()
while s != '0':
    answer = 0
    len_s = len(s)
    for start in range(len_s):
        for end in range(start + 1, min(len_s, start + 7)):
            v = int(s[start:end])
            if 2 <= v <= 100000 and is_prime(v):
                answer = max(answer, v)
    print(answer)
    s = sys.stdin.readline().rstrip()
