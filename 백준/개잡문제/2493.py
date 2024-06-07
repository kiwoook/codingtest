import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

top_list2 = [(idx, value) for idx, value in enumerate(map(int, sys.stdin.readline().rstrip().split()))]

answer = [0 for _ in range(n)]

idx1, value1 = top_list2.pop()
q = deque([(idx1, value1)])

while top_list2:
    idx, value = top_list2.pop()
    if value < q[0][1]:
        q.appendleft((idx, value))
    else:
        while q and q[0][1] <= value:
            i, v = q.popleft()
            answer[i] = idx + 1
        q.appendleft((idx, value))

print(*answer)
