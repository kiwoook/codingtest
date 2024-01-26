from itertools import product

n, m = map(int, input().split())
a = list(set(map(int, input().split())))

product_a = list(product(a, repeat=m))

answer = set()
for value in product_a:
    value = list(value)
    value.sort()
    answer.add(tuple(value))

answer = list(answer)
answer.sort()

for a in answer:
    print(*a)
