import sys

n = int(sys.stdin.readline().rstrip())

meeting_time = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

meeting_time.sort(key=lambda x: (x[0], x[1]))

# 모두 진행해야 함

meeting_end_time_room = [meeting_time[0][1]]

for start_time, end_time in meeting_time[1:]:
    sw = False
    # 리스트의 크기가 곧 답이다.
    for idx, meeting_end_time in enumerate(meeting_end_time_room):
        if meeting_end_time <= start_time:
            meeting_end_time_room[idx] = end_time
            sw = True
            break

    if not sw:
        meeting_end_time_room.append(end_time)

print(len(meeting_end_time_room))
