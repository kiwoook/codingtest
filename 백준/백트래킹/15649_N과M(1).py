def recur(depth, max_depth, branch, arr):
    global visited, n

    if depth == max_depth:
        print(' '.join(arr))
        return

    for i in range(1, n + 1):
        if visited[i] == 0:
            arr.append(str(i))
            visited[i] = 1
            recur(depth + 1, m - 1, i, arr)
            visited[i] = 0
            arr.pop()


n, m = map(int, input().split())

visited = [0 for _ in range(n + 1)]
a = []

for i in range(1, n + 1):
    a.append(str(i))
    visited[i] = 1
    recur(0, m - 1, i, a)
    visited[i] = 0
    a.pop()
