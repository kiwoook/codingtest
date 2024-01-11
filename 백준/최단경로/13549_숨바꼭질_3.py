from collections import deque

n, k = map(int, input().split())

distance = [0 for _ in range(100001)]
visited = [0 for _ in range(100001)]

q = deque([n])

while q:

    # 제일 최소값으로 저장되게 해야하는디
    x = q.popleft()
    if x == k:
        print(distance[k])
        break

    if x == 0:
        distance[x + 1] = distance[x] + 1
        q.append(x + 1)
        visited[x + 1] = 1
    else:
        if 0 <= 2 * x < 100001:
            if visited[2 * x] == 0:
                distance[2 * x] = distance[x]
                q.append(2 * x)
                visited[2 * x] = 1
            else:
                if distance[2 * x] >= distance[x]:
                    distance[2 * x] = distance[x]
                    q.append(2 * x)

        if 0 <= x - 1 < 100001:
            if visited[x - 1] == 0:
                distance[x - 1] = distance[x] + 1
                q.append(x - 1)
                visited[x - 1] = 1
            else:
                if distance[x - 1] >= distance[x] + 1:
                    distance[x - 1] = distance[x] + 1
                    q.append(x - 1)

        if 0 <= x + 1 < 100001:
            if visited[x + 1] == 0:
                distance[x + 1] = distance[x] + 1
                q.append(x + 1)
                visited[x + 1] = 1
            else:
                if distance[x + 1] >= distance[x] + 1:
                    distance[x + 1] = distance[x] + 1
                    q.append(x + 1)
