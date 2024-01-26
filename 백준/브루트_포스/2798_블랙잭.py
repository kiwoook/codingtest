from itertools import combinations

n, m = map(int, input().split())

a = list(map(int, input().split()))

comb = list(filter(lambda x: sum(x) <= m, list(combinations(a, 3))))

comb.sort(key=lambda x: sum(x))

print(sum(comb[-1]))
