from collections import deque


def solution(queue1, queue2):
    answer = 0
    len_queue1 = len(queue1)
    len_queue2 = len(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    total_1 = sum(queue1)
    total_2 = sum(queue2)
    result = (total_1 + total_2) / 2

    while total_1 != result or total_2 != result:
        if (len_queue1 + len_queue2)*4 <= answer:
            return -1
        if total_1 > total_2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            total_1 -= tmp
            total_2 += tmp
            len_queue1 -= 1
            len_queue2 += 1
            answer += 1
            continue
        elif total_1 < total_2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            total_1 += tmp
            total_2 -= tmp
            len_queue1 += 1
            len_queue2 -= 1
            answer += 1

        if len_queue1 == 1 and total_1 > total_2 or len_queue2 == 1 and total_1 < total_2:
            return -1

    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
