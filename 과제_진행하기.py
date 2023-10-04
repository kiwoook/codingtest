from collections import deque


def solution(plans):
    answer = []
    waiting = []

    plans.sort(key=lambda x: x[1])
    for idx, plan in enumerate(plans):
        name, start, playtime = plan
        hour, minute = start.split(":")
        start = int(hour) * 60 + int(minute)
        plans[idx] = [name, start, int(playtime)]
    plans = deque(plans)

    doing_name, doing_start, doing_playtime = plans.popleft()
    while plans or waiting:
        if plans:
            next_name, next_start, next_playtime = plans.popleft()
            free_time = next_start - doing_start
            if free_time >= doing_playtime:
                free_time = free_time - doing_playtime
                answer.append(doing_name)
                while waiting and free_time > 0:
                    waiting_name, waiting_time = waiting.pop()
                    if free_time > waiting_time:
                        free_time -= waiting_time
                        answer.append(waiting_name)
                    else:
                        waiting.append([waiting_name, waiting_time - free_time])
                        break
            else:
                waiting.append([doing_name, doing_playtime - free_time])
            if not plans:
                answer.append(next_name)
            doing_name, doing_start, doing_playtime = next_name, next_start, next_playtime

        elif waiting:
            answer.append(waiting.pop()[0])

    return answer


print(solution(
    [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
))
