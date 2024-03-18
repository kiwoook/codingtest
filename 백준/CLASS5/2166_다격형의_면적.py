import sys

n = int(sys.stdin.readline().rstrip())

points = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    points.append([x, y])

points.append(points[0])

one = 0
two = 0
for i in range(n):
    one += points[i][0] * points[i + 1][1]
    two += points[i][1] * points[i + 1][0]

print(round(abs((one - two) / 2), 1))
