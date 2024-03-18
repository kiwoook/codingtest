import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))

perm_list = sorted(list(set(permutations(a, m))))

for perm in perm_list:
    print(*perm)

