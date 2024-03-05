import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

stack = []
queue_stack = deque([])
sw_queue_stack = []
tmp = list(map(int, sys.stdin.readline().rstrip().split()))

for t in tmp:
    sw_queue_stack.append(t)

tmp = list(map(int, sys.stdin.readline().rstrip().split()))

for t in tmp:
    stack.append(t)

for idx, value in enumerate(stack):
    if sw_queue_stack[idx] == 0:
        queue_stack.append(value)

m = int(sys.stdin.readline().rstrip())
insert_list = list(map(int, sys.stdin.readline().rstrip().split()))

answer_list = []

if queue_stack:
    for insert_value in insert_list:
        answer_list.append(queue_stack.pop())
        queue_stack.appendleft(insert_value)
else:
    for insert_value in insert_list:
        answer_list.append(insert_value)

print(*answer_list)
