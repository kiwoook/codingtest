import sys


def dfs(depth, visited):
    global answer

    if depth == n:
        if not any(visited):
            return

        if sum(num_list[i] for i in range(n) if visited[i]) == s:
            answer += 1
        return

    visited[depth] = 1
    dfs(depth + 1, visited)
    visited[depth] = 0
    dfs(depth + 1, visited)


answer = 0
n, s = map(int, sys.stdin.readline().rstrip().split())
num_list = list(map(int, sys.stdin.readline().rstrip().split()))

dfs(0, [0 for _ in range(n)])

print(answer)
