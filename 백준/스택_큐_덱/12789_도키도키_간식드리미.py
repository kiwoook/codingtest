n = int(input())
line_stack = list(map(int, input().split()))
line_stack.reverse()
tmp = []
cnt = 1
sw = 0

while len(line_stack) != 0 or len(tmp) != 0:
    if len(line_stack) == 0 and len(tmp) > 0 and tmp[-1] != cnt:
        sw = 1
        break
    if len(line_stack) > 0 and line_stack[-1] == cnt:
        line_stack.pop()
        cnt += 1
    else:
        if len(tmp) > 0 and tmp[-1] == cnt:
            tmp.pop()
            cnt += 1
        else:
            tmp.append(line_stack.pop())
if sw:
    print("Sad")
else:
    print("Nice")
