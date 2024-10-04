def dfs(arr, depth):
    global sequence_list
    mid = (len(arr) // 2)
    answer[depth].append(arr[mid])

    if depth == k - 1:
        return

    dfs(arr[:mid], depth + 1)
    dfs(arr[mid + 1:], depth + 1)


k = int(input())
sequence_list = list(map(int, input().split()))

answer = [[] for _ in range(k)]

dfs(sequence_list, 0)

for ans in answer:
    print(*ans)

