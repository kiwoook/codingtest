import sys
from collections import deque


def D(value):
    value = 2 * value % 10000
    return value


def S(value):
    if value == 0:
        return 9999
    return value - 1


def L(value):
    return value // 1000 + (value % 1000) * 10


def R(value):
    return value // 10 + (value % 10) * 1000


def bfs(value, target):
    global visited, global_answer

    q = deque([(value, '')])

    while q:
        value, answer = q.popleft()
        if value == target:
            return answer
        if visited[value] == 1:
            continue
        visited[value] = 1

        d_value = D(value)
        s_value = S(value)
        r_value = R(value)
        l_value = L(value)
        if visited[d_value] == 0:
            q.append((d_value, answer + 'D'))
        if visited[s_value] == 0:
            q.append((s_value, answer + 'S'))
        if visited[r_value] == 0:
            q.append((r_value, answer + 'R'))
        if visited[l_value] == 0:
            q.append((l_value, answer + "L"))


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    visited = [0 for _ in range(10000)]
    global_answer = ''
    n, target = map(int, sys.stdin.readline().rstrip().split())
    print(bfs(n, target))

