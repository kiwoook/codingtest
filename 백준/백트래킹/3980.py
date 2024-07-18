import sys

answer = 0


def dfs(depth, total):
    global answer, visited, player_list
    if depth == 11:
        answer = max(answer, total)
        return

    for p in range(11):
        if not visited[p] and player_list[depth][p] > 0:
            visited[p] = True
            dfs(depth + 1, total + player_list[depth][p])
            visited[p] = False  


C = int(sys.stdin.readline().rstrip())

for _ in range(C):
    player_list = []
    for _ in range(11):
        player_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

    visited = [False] * 11
    answer = 0
    dfs(0, 0)
    print(answer)
