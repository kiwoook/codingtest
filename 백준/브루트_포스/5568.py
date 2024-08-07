import sys


def dfs(depth, value):
    global answer_set, visited

    if depth == k:
        answer_set.add(value)
        return

    for idx, num in enumerate(num_list):
        if not visited[idx]:
            visited[idx] = True
            dfs(depth + 1, value + num)
            visited[idx] = False


n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
num_list = []
answer_set = set()

for _ in range(n):
    num_list.append(sys.stdin.readline().rstrip())

visited = [False] * n
dfs(0, '')

print(len(answer_set))
