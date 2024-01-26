import sys

n = int(input())

arr = []

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    arr.append(tmp)

arr.sort(key=lambda x: (x[0], x[1]))

for a in arr:
    print(*a)
