import sys

INF = 1e9
min_x, min_y, max_x, max_y = INF, INF, -INF, -INF
dot_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(int(sys.stdin.readline().rstrip()))]

for y, x in dot_list:
    min_x, min_y = min(min_x, x), min(min_y, y)
    max_x, max_y = max(max_x, x), max(max_y, y)

print((max_y - min_y) * (max_x - min_x))
