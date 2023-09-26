graph = []


def recur(pos, n, route_node):
    global graph

    for k in range(n + 1):
        if graph[pos][k] == 1:
            graph[route_node][k] = -1
            graph[k][route_node] = -1
            recur(k, n, route_node)


def solution(n, results):
    global graph
    answer = 0
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1,n+1):
        graph[i][i] = -1

    for [y, x] in results:
        graph[y][x] = 1
        graph[x][y] = -1

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1

    for i in range(1, n + 1):
        if all(graph[i][j] != 0 for j in range(1, n + 1)):
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
