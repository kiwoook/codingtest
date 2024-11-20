import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    answer = ''
    s = sys.stdin.readline().rstrip()

    left_q = deque([])
    right_q = deque([])

    for char in s:
        if char == '<':
            if left_q:
                right_q.appendleft(left_q.pop())
        elif char == '>':
            if right_q:
                left_q.append(right_q.popleft())
        elif char == '-':
            if left_q:
                left_q.pop()
        else:
            left_q.append(char)

    print(''.join(left_q) + ''.join(right_q))
