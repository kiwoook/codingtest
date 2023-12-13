def recur(depth, branch, arr):
    global n, m

    if depth >= 1 and int(arr[-2]) > branch:
        return

    if depth == m -1:
        print(' '.join(arr))
        return

    for i in range(1, n+1):
        arr.append(str(i))
        recur(depth+1, i, arr)
        arr.pop()


n, m = map(int, input().split())
arr = []

for i in range(1, n+1):
    arr.append(str(i))
    recur(0, i, arr)
    arr.pop()