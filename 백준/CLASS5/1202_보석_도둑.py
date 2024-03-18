import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

a = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().rstrip().split())
    a.append((m / v, m, v))

a.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)

for _ in range(k):
    # 가방 별 최대 무게
    c = int(sys.stdin.readline().rstrip())

