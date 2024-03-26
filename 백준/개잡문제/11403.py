import sys


def change_value(value):
    value = int(value)
    if value == 0:
        return INF
    return value


INF = int(1e9)

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(change_value, sys.stdin.readline().rstrip().split())))

for middle in range(n):
    for start in range(n):
        for end in range(n):
            if graph[start][end] > graph[start][middle] + graph[middle][end]:
                graph[start][end] = 1

for i in range(n):
    for k in range(n):
        if graph[i][k] == INF:
            print("0", end=' ')
        else:
            print(graph[i][k], end=' ')
    print()
