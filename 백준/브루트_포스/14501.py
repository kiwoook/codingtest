import sys

answer = 0


def dfs(day, price):
    global answer

    if day > n:
        return

    answer = max(answer, price)

    for i in range(day, n):
        if i + work_list[i][0] <= n:
            dfs(i + work_list[i][0], price + work_list[i][1])


n = int(sys.stdin.readline().rstrip())
work_list = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dfs(0, 0)
print(answer)
