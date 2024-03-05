import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
crr = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [[0 for _ in range(n + 1)] for _ in range(sum(crr) + 1)]





