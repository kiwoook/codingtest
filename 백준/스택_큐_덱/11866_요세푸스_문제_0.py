from collections import deque

n, pointer = map(int, input().split())
queue = deque([i for i in range(1, n + 1)])
pointer -= 1
answer = []

idx = 0
while queue:
    if idx == pointer:
        answer.append(str(queue.popleft()))
        idx = -1
    else:
        queue.append(queue.popleft())

    idx += 1

print("<%s>" % (', '.join(answer)))
