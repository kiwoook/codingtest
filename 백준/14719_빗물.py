height, width = map(int, input().split())

arr = list(map(int, input().split()))

answer = 0

world = [[0 for _ in range(width)] for _ in range(height)]

for i in range(width):
    for k in range(height - arr[i], height):
        world[k][i] = 1

for i in range(height - 1, -1, -1):
    start_idx = -1
    for k in range(width):
        if start_idx >= 0 and world[i][k] == 1:
            answer += k - start_idx - 1
            start_idx = k
            continue
        if world[i][k] == 1:
            start_idx = k

print(answer)
