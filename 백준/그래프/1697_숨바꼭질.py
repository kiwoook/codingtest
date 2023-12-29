from collections import deque

n, k = map(int, input().split())

distance = [0 for _ in range(100001)]

q = deque([n])
cnt = 0

while q:
    # 값이 0 일때를 분기
    x = q.popleft()
    if x == k:
        print(distance[k])
        break

    if x == 0:
        distance[x + 1] = distance[x] + 1
        q.append(x + 1)
    else:
        if 0 <= x - 1 < 100001:
            if distance[x - 1] == 0 or distance[x - 1] == distance[x] + 1:
                distance[x - 1] = distance[x] + 1
                q.append(x - 1)

        if 0 <= x + 1 < 100001:
            if distance[x + 1] == 0 or distance[x + 1] == distance[x] + 1:
                distance[x + 1] = distance[x] + 1
                q.append(x + 1)

        if 0 <= 2 * x < 100001:
            if distance[2 * x] == 0 or distance[2 * x] == distance[x] + 1:
                distance[2 * x] = distance[x] + 1
                q.append(2 * x)
