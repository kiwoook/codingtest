from collections import deque


def solution(menu, order, k):
    answer = 1
    person_waiting = 0
    time = 0
    make_end_time = 0
    order_q = deque(order)
    waiting_q = deque([])
    if len(order) == 1:
        return 1

    while order_q or waiting_q:

        # time 이 k로 나눠지면 새로운 주문이 들어온다.
        print(person_waiting, make_end_time, time)

        if time % k == 0 and order_q:
            person_waiting += 1
            waiting_q.append(order_q.popleft())

        # make_end_time보다 time이 크거나 같고 waiting_q에 없으면 order_q에서 빼낸다.
        if make_end_time <= time:
            if waiting_q:
                idx = waiting_q.popleft()
                make_end_time = time + menu[idx]
                if 0 < time:
                    person_waiting -= 1

        answer = max(answer, person_waiting)

        time += 1

    return answer

# 그냥 1초마다 하는게 나을거같음

print(solution([5, 12, 30], [1, 2, 0, 1], 10))