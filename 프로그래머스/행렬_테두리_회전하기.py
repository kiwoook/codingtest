from collections import deque

arr = []


def rotate(y1, x1, y2, x2):
    global arr
    stack = deque([])

    for k in range(x1, x2):
        stack.append(arr[y1][k])
    for i in range(y1, y2 + 1):
        stack.append(arr[i][x2])
    for k in range(x2 - 1, x1 - 1, -1):
        stack.append(arr[y2][k])
    for i in range(y2 - 1, y1, -1):
        stack.append(arr[i][x1])

    stack.appendleft(stack.pop())
    min_value = min(stack)

    idx = 0
    for k in range(x1, x2):
        arr[y1][k] = stack[idx]
        idx += 1
    for i in range(y1, y2 + 1):
        arr[i][x2] = stack[idx]
        idx += 1
    for k in range(x2 - 1, x1 - 1, -1):
        arr[y2][k] = stack[idx]
        idx += 1
    for i in range(y2 - 1, y1, -1):
        arr[i][x1] = stack[idx]
        idx += 1

    return min_value


def solution(rows, columns, queries):
    global arr
    answer = []
    arr = [[0] * columns for _ in range(rows)]
    v = 1

    for i in range(rows):
        for k in range(columns):
            arr[i][k] = v
            v += 1

    for query in queries:
        y1, x1, y2, x2 = query
        answer.append(rotate(y1 - 1, x1 - 1, y2 - 1, x2 - 1))

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
