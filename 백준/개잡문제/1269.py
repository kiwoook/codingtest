import sys

m, n = map(int, sys.stdin.readline().rstrip().split())
a = set(map(int, sys.stdin.readline().rstrip().split()))
b = set(map(int, sys.stdin.readline().rstrip().split()))

print(len(a.union(b) - (a & b)))
