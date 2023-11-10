from collections import deque


def solution(n, t, m, timetable):
    last_time = 9 * 60 + t * (n - 1)

    for idx, time in enumerate(timetable):
        timetable[idx] = int(time[:2]) * 60 + int(time[3:])

    timetable.sort()

    queue = deque(timetable)

    # 마지막 버스 시간 전까지 타야 될 사람들 미리 처리
    for i in range(0, n - 1):
        compare_time = 9 * 60 + t * i
        people = 0
        while queue[0] <= compare_time:
            queue.popleft()
            people += 1
            if people == m:
                break

    queue = deque(sorted(queue, reverse=True))

    # 마지막 버스 시간을 탑승할 수 없는 사람들 처리
    while queue:
        if queue[0] > last_time:
            queue.popleft()
        else:
            break

    if len(queue) >= m:
        answer = queue[-m] - 1
    else:
        answer = last_time

    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(10, 60, 45,
               ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                "23:59", "23:59", "23:59", "23:59", "23:59"]))
print(solution(10, 25, 1, ["09:00", "09:10", "09:20", "09:30", "09:40", "09:50",
                           "10:00", "10:10", "10:20", "10:30", "10:40", "10:50"]))
