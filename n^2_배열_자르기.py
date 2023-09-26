from collections import deque


def solution(n, left, right):
    n_list = [[0] * n for _ in range(n)]

    stack = deque([(0, 0, 1)])
    dy = [0, 1, 1]
    dx = [1, 0, 1]
    while stack:
        y, x, j = stack.popleft()
        if n_list[y][x] != 0:
            continue
        n_list[y][x] = j

        for i in range(3):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                stack.append((ny, nx, j + 1))

    arr = sum(n_list, [])

    return arr[left:right + 1]


print(solution(100, 7, 14))
