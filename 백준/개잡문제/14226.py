from collections import deque

INF = int(1e12)
s = int(input())

answer = INF

q = deque([(1, 0, 0)])
min_visited = [[INF for _ in range(1001)] for _ in range(1001)]

while q:
    value, copy_value, time = q.popleft()
    if value == s:
        answer = min(answer, time)
    if value > s or value < 1:
        continue
    # 현재 시간 값이 더 작다면 진입한다.
    if min_visited[value][copy_value] > time:
        min_visited[value][copy_value] = time
        q.append((value, value, time + 1))
        q.append((value + copy_value, copy_value, time + 1))
        q.append((value - 1, copy_value, time + 1))

print(answer)
