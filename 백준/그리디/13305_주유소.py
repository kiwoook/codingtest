import sys

cost = 0
n = int(input())
distance = list(map(int, sys.stdin.readline().rstrip().split()))
station = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
pos = station[0]

for idx, s in enumerate(station[1:]):
    if pos >= s:
        cost += sum(distance[start:idx+1]) * pos
        start = idx+1
        pos = s
cost += sum(distance[start:]) * pos

print(cost)
