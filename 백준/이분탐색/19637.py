import sys

n, m = map(int, input().split())

rank = []

for i in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    b = int(b)
    rank.append((b, i, a))

rank.sort(key=lambda x: (x[0], x[1]))

for _ in range(m):
    x = int(sys.stdin.readline().rstrip())

    left = 0
    right = len(rank) - 1

    while left < right:
        mid = (left + right) // 2

        if rank[mid][0] >= x:
            right = mid
        else:
            left = mid + 1

    print(rank[left][2])
