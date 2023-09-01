from collections import deque


def solution(book_time):
    answer = 0
    time_len = len(book_time)
    queue = [deque() for _ in range(time_len)]
    print(queue)
    for idx, [start, end] in enumerate(book_time):
        start_hour, start_min = start.split(":")
        end_hour, end_min = end.split(":")
        start_time = int(start_hour) * 60 + int(start_min)
        end_time = int(end_hour) * 60 + int(end_min)
        book_time[idx][0] = start_time
        book_time[idx][1] = end_time + 10

    book_time.sort(key=lambda x: (x[0], -x[1]))

    for [start, end] in book_time:
        for i in range(time_len):
            sw = 0
            if len(queue[i]) == 0:
                queue[i].append(end)
                break
            for q in queue[i]:
                if q <= start:
                    queue[i].popleft()
                    queue[i].append(end)
                    sw = 1
                    break
            if sw:
                break
    for r in queue:
        if len(r) != 0:
            answer += 1

    return answer


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))
print(solution([["09:10", "10:10"], ["10:20", "12:20"], ["12:30", "13:20"]]))
