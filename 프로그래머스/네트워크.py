path = []


def dfs(computers, to, n):
    for i in range(n):
        if not path[i] and computers[to][i] == 1:
            path[i] = True
            dfs(computers, i, n)


def solution(n, computers):
    global path
    answer = 0
    path = [False] * n
    while not all(path):
        for i in range(n):
            if not path[i]:
                path[i] = True
                dfs(computers, i, n)
                answer += 1
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

