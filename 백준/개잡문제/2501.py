n, k = map(int, input().split())

cnt = 0
sw = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        sw = 1
        break

if sw == 0:
    print(0)
