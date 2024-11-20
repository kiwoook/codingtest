import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
q = deque([i for i in range(1, n + 1)])
tartget_list = list(map(int, sys.stdin.readline().rstrip().split()))

answer = 0

for target_value in tartget_list:
    target_idx = q.index(target_value)

    if target_idx == 0:
        q.popleft()
        continue
    if target_idx <= len(q) // 2:
        while q[0] != target_value:
            answer += 1
            q.append(q.popleft())
        q.popleft()
        continue
    if target_idx > len(q) // 2:
        while q[0] != target_value:
            answer += 1
            q.appendleft(q.pop())
        q.popleft()

print(answer)
