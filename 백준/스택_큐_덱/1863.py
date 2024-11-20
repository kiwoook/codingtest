import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

building_list = deque([int(sys.stdin.readline().rstrip().split()[1]) for _ in range(n)])

stack = [0]
answer = 0
while building_list:
    v = building_list.popleft()

    if stack[-1] < v:
        answer += 1
        stack.append(v)
    else:
        # 스택 마지막값이 v보다 크다면 pop한다.
        while stack and stack[-1] > v:
            stack.pop()

        if stack and stack[-1] != v:
            answer += 1
        stack.append(v)

print(answer)
