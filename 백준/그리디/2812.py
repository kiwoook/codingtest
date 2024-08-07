import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
number = list(map(int, list(sys.stdin.readline().rstrip())))

stack = []
cnt = 0

for num in number:
    while stack and cnt < k and stack[-1] < num:
        stack.pop()
        cnt += 1
    stack.append(num)

while cnt < k:
    stack.pop()
    cnt += 1

print(''.join(map(str, stack)))
