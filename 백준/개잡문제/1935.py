import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

exp = list(sys.stdin.readline().rstrip())

num_list = []

for _ in range(n):
    num_list.append(int(sys.stdin.readline().rstrip()))

for idx1, num in enumerate(num_list):
    for idx2, value in enumerate(exp):
        if type(value) is str and value.isalpha() and ord(value) - ord('A') == idx1:
            exp[idx2] = num

q = deque(exp)
stack = []
while q:
    v = q.popleft()
    if type(v) is int:
        stack.append(v)
    else:
        v1 = stack.pop()
        v2 = stack.pop()
        if v == '*':
            stack.append(v2 * v1)
        elif v == '+':
            stack.append(v2 + v1)
        elif v == '/':
            stack.append(v2 / v1)
        elif v == '-':
            stack.append(v2 - v1)

print("{:.2f}".format(stack[0]))
