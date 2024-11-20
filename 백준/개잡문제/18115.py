from collections import deque

n = int(input())
card_list = [i for i in range(1, n + 1)]
cmd_list = list(map(int, input().split()))

answer = deque([])
for v in card_list:
    cmd = cmd_list.pop()

    if cmd == 1:
        answer.appendleft(v)
    elif cmd == 2:
        tmp = answer.popleft()
        answer.appendleft(v)
        answer.appendleft(tmp)
    elif cmd == 3:
        answer.append(v)

print(*answer)
