from collections import deque

n, m = map(int, input().split())
a = deque(sorted(list(map(int, input().split()))))
b = deque(sorted(list(map(int, input().split()))))





print(*sorted(a + b))
