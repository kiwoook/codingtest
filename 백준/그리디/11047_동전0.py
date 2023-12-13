n, k = map(int, input().split())

cnt = 0

coin = []

for i in range(n):
    coin.append(int(input()))

while k != 0:
    for i in range(n-1, -1 ,-1):
        if k >= coin[i]:
            cnt += k // coin[i]
            k %= coin[i]
            break

print(cnt)
