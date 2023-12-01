from collections import deque

n = int(input())
queue = deque(enumerate(map(int, input().split())))

answer = []

while queue:
    idx, move = queue.popleft()
    answer.append(str(idx + 1))

    if move > 0:
        queue.rotate(-(move - 1))
    if move < 0:
        queue.rotate(-move)

print(' '.join(answer))

