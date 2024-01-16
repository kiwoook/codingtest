from itertools import permutations

n, m = map(int, input().split())
a = list(map(int, input().split()))

permu = list(permutations(a, m))

permu.sort()

for p in permu:
    print(*p)