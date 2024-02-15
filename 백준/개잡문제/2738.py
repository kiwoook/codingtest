n, m = map(int, input().split())

a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split())))
for _ in range(n):
    b.append(list(map(int, input().split())))

answer = [[x + y for x, y in zip(i, u)] for i, u in zip(a, b)]
for x in range(n):
    print(*answer[x])
