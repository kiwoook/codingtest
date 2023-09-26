from collections import deque


def solution(order):
    order_len = len(order)
    order = deque(order)
    cnt = 0
    assist = deque()
    box_line = deque([(i + 1) for i in range(order_len)])

    while len(order) != 0:
        target = order.popleft()
        if len(box_line) == 0 and len(assist) > 0 and assist[0] != target:
            break
        if len(assist) > 0 and assist[0] == target:
            assist.popleft()
            cnt += 1
            continue
        else:
            value = 0
            sw = 0
            while value != target:
                if len(box_line) == 0:
                    sw = 1
                    break
                value = box_line.popleft()
                assist.appendleft(value)
            if not sw:
                assist.popleft()
                cnt += 1

    return cnt


print(solution([4, 3, 1, 2, 5]))

print(solution([5, 4, 3, 2, 1]))