import sys
from collections import defaultdict

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    wear_dict = defaultdict(int)
    for _ in range(n):
        a, b = sys.stdin.readline().rstrip().split()
        wear_dict[b] += 1

    answer = 1

    for value in wear_dict.values():
        answer *= value + 1

    print(answer - 1)
