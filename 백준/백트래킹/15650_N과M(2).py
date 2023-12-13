def recur(depth, branch, arr):
    global n, m, visited

    if depth > 1 and int(arr[-2]) >= int(branch):
        return

    if depth == m:
        print(' '.join(arr))
        return

    for i in range(branch, n + 1):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(str(i))
            recur(depth+1, i, arr)
            arr.pop()
            visited[i] = 0


n, m = map(int, input().split())
arr = []

visited = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    visited[i] = 1
    arr.append(str(i))
    recur(1, i, arr)
    arr.pop()
    visited[i] = 0
