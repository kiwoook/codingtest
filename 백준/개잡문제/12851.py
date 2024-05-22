from collections import deque

INF = int(1e9)

pos_list = [INF for _ in range(100001)]

n, k = map(int, input().split())

q = deque([(n, 0)])

answer = INF
cnt = 0

while q:
    pos, sec = q.popleft()
    pos_list[pos] = sec
    if pos == k:
        if answer > sec:
            answer = sec
            cnt = 0
        if answer == sec:
            cnt += 1

    if 0 <= 2 * pos <= 100000 and pos_list[2 * pos] >= sec + 1:
        q.append((2 * pos, sec + 1))
    if 0 <= pos - 1 <= 100000 and pos_list[pos - 1] >= sec + 1:
        q.append((pos - 1, sec + 1))
    if 0 <= pos + 1 <= k and pos_list[pos + 1] >= sec + 1:
        q.append((pos + 1, sec + 1))

print(answer)
print(cnt)
