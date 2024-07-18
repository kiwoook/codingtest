import sys

n = int(sys.stdin.readline().rstrip())

t_shirt_list = list(map(int, sys.stdin.readline().rstrip().split()))

t, p = map(int, sys.stdin.readline().rstrip().split())

print(sum(((t_shirt - 1) // t + 1) for t_shirt in t_shirt_list))
print(n // p, n % p)
