from collections import deque

n, k = map(int, input().split())
answer = []
q = deque([i for i in range(1, n + 1)])

while len(q) != 0:
    for _ in range(k - 1):
        q.append(q.popleft())

    answer.append(q.popleft())

answer = ', '.join(map(str, answer))

print("<" + answer + ">")
