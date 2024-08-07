import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
muscle_q = deque(sorted(list(map(int, sys.stdin.readline().rstrip().split()))))
answer = 0

if n % 2 == 0:
    while muscle_q:
        answer = max(answer, muscle_q.popleft() + muscle_q.pop())
if n % 2 == 1:
    answer = muscle_q.pop()
    while muscle_q:
        answer = max(answer, muscle_q.popleft() + muscle_q.pop())

print(answer)