import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
child_list = list(map(int, sys.stdin.readline().rstrip().split()))

diff = []
for i in range(1, n):
    diff.append(abs(child_list[i] - child_list[i - 1]))

diff.sort()

print(sum(diff[:n - k]))
