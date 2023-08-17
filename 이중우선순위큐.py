from collections import deque


def solution(operations):
    q = deque()

    for operation in operations:
        command, num = operation.split(" ")
        if len(q) == 0:
            continue
        if command == 'I':
            q.append(int(num))
        elif num == '1':
            q.popleft()
        elif num == '-1':
            q.pop()
        print(q)
        q = deque(sorted(q))

    if len(q) == 0:
        return [0, 0]
    elif len(q) == 1:
        value = q.pop()
        return [value, value]
    else:
        return [q.popleft(), q.pop()]

