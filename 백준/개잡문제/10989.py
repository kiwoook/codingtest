import sys

cnt = [0 for _ in range(10001)]
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    v = int(sys.stdin.readline().rstrip())
    cnt[v] += 1

for i in range(1, 10001):
    while cnt[i] != 0:
        print(i)
        cnt[i] -= 1
