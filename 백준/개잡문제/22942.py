import sys

n = int(sys.stdin.readline().rstrip())
circle_list = []
for idx in range(n):
    x, r = map(int, sys.stdin.readline().rstrip().split())
    circle_list.append((x - r, idx))
    circle_list.append((x + r, idx))

circle_list.sort()
stack = []

for v, idx in circle_list:
    if stack:
        # 스택이 있으면
        if stack[-1] == idx:
            stack.pop()
        else:
            stack.append(idx)
    else:
        stack.append(idx)

if stack:
    print("NO")
else:
    print("YES")
