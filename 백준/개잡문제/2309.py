import sys


def dfs(depth, hap):
    global answer, sw, visited

    if sw == 1:
        return

    if depth == 6:
        if hap == 100:
            answer = [height_list[i] for i in range(9) if visited[i] == 1]
            sw = 1

        return

    for i in range(9):
        if visited[i] == 0:
            visited[i] = 1
            dfs(depth + 1, hap + height_list[i])
            visited[i] = 0


sw = 0
height_list = []
answer = []
visited = [0 for _ in range(9)]

for _ in range(9):
    height_list.append(int(sys.stdin.readline().rstrip()))

for idx in range(9):
    visited[idx] = 1
    dfs(0, height_list[idx])
    visited[idx] = 0

answer.sort()

for ans in answer:
    print(ans)
