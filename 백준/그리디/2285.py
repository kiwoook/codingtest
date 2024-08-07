import sys

n = int(sys.stdin.readline().rstrip())
town_list = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

town_list.sort(key=lambda x: (-x[1], x[0]))

