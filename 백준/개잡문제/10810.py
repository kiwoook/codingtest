n, m = map(int, input().split())

a = [0 for _ in range(n + 1)]
for _ in range(m):
    i, j, k = map(int, input().split())
    a[i:j + 1] = [k] * (j - i + 1)

print(*a[1:len(a)])
