from itertools import combinations_with_replacement

answer = []

n, m = map(int, input().split())
a = list(map(int, input().split()))

permu = list(combinations_with_replacement(a, m))

for p in permu:
    x = list(p)
    x.sort()
    answer.append(x)

answer.sort()

for a in answer:
    print(*a)
