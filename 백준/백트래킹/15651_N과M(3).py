def recur(depth, arr):
    global n, m

    if depth == m -1:
        print(' '.join(arr))
        return

    for i in range(1, n+1):
        arr.append(str(i))
        recur(depth+1, arr)
        arr.pop()


n, m = map(int, input().split())
arr = []

for i in range(1, n+1):
    arr.append(str(i))
    recur(0, arr)
    arr.pop()
