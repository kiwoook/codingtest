import sys

n = int(sys.stdin.readline().rstrip())
answer = 0

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    stack = [s[0]]
    for value in s[1:]:
        if stack and stack[-1] == value:
            stack.pop()
        else:
            stack.append(value)
    if len(stack) == 0:
        answer += 1

print(answer)
