from collections import deque


def solution(x, y, n):
    answer = -1
    queue = deque([(y, 0)])
    failed_count = 0
    sw = 0
    while queue:
        curr_y, depth = queue.popleft()
        if curr_y == x:
            answer = depth
            break
        if curr_y < 1 :
            break

        queue.append((curr_y - n, depth + 1))
        if curr_y % 2 == 0:
            queue.append((curr_y / 2, depth+1))
        if curr_y % 3 == 0:
            queue.append((curr_y /3, depth + 1))

    return answer


print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))
