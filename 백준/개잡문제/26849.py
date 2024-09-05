import sys

n = int(sys.stdin.readline().rstrip())

INF = int(1e12)
max_answer, min_answer = 0, INF
total = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    value = a / b
    max_answer = max(max_answer, value)
    min_answer = min(min_answer, value)
    total += a / b

print("%.6f %.6f %.6f" % (min_answer, max_answer, total))
