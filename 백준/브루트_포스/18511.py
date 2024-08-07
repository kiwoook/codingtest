import sys


def dfs(value, depth):
    global answer

    if depth > len_n:
        return

    if 0 < depth <= len_n and int(value) <= n:
        answer = max(answer, int(value))

    for num in num_list:
        dfs(value + num, depth + 1)


n, k = map(int, sys.stdin.readline().rstrip().split())
len_n = len(str(n))
num_list = list(sys.stdin.readline().rstrip().split())

answer = 0
dfs('', 0)

print(answer)