n = int(input())

max_5coin = n // 5

for coin5 in range(max_5coin, -1, -1):
    if (n - 5 * coin5) % 2 == 0:
        print(coin5 + (n - 5 * coin5) // 2)
        exit(0)

print(-1)
