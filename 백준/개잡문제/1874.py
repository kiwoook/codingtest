import sys

n = int(sys.stdin.readline().rstrip())

stack1 = [i for i in range(n, 0, -1)]
stack2 = []

target_stack = []
answer = []

for _ in range(n):
    target_stack.append(int(sys.stdin.readline().rstrip()))

target_idx = 0
while target_idx < len(target_stack):
    # 만약 value가 스택[idx]값보다 작다면 도달할때까지 늘린다.
    if stack1 and stack1[-1] <= target_stack[target_idx]:
        while stack1 and stack1[-1] <= target_stack[target_idx]:
            stack2.append(stack1.pop())
            answer.append('+')

    if stack2 and target_stack[target_idx] == stack2[-1]:
        answer.append('-')
        stack2.pop()
        target_idx += 1
    else:
        print("NO")
        exit(0)

for ans in answer:
    print(ans)
