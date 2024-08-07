import math
import sys

n = int(sys.stdin.readline().rstrip())
gap_list, tree_list = [], [int(sys.stdin.readline().rstrip()) for _ in range(n)]
answer = 0

tree_list.sort()

for i in range(1, n):
    gap_list.append(tree_list[i] - tree_list[i - 1])

gcd = math.gcd(*set(gap_list))

for gap in gap_list:
    answer += gap // gcd - 1

print(answer)
