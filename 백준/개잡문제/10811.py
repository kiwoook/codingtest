n, m = map(int, input().split())

basket = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    basket[a:b + 1] = basket[a:b + 1][::-1]

print(*basket[1::])
