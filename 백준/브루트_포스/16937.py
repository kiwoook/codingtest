import sys

answer = 0


def dfs(r, c, area, depth):
    global answer

    if depth == 2:
        if r <= h and c <= w:
            answer = max(answer, area)
        return

    for idx, (a, b) in enumerate(sticker_list):
        if not visited[idx]:
            visited[idx] = True
            dfs(r + a, max(c, b), area + (a * b), depth + 1)
            dfs(r + b, max(c, a), area + (a * b), depth + 1)
            dfs(max(r, a), c + b, area + (a * b), depth + 1)
            dfs(max(r, b), c + a, area + (a * b), depth + 1)
            visited[idx] = False


h, w = map(int, sys.stdin.readline().rstrip().split())
n = int(sys.stdin.readline().rstrip())
sticker_list = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [False for _ in range(n)]

dfs(0, 0, 0, 0)

print(answer)
