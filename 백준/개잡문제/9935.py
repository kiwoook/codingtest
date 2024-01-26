from collections import deque

target = list(input())
check = input()
q = deque(target)
len_check = len(check)

stack = []
while q:
    v = q.popleft()
    stack.append(v)

    if len(stack) >= len_check:
        sw = 0
        for i in range(len_check):
            if stack[-(i+1)] != check[-(i+1)]:
                sw = 1
                break
        if sw == 0:
            for _ in range(len_check):
                stack.pop()


if len(stack) != 0:
    print(''.join(stack))
else:
    print("FRULA")
