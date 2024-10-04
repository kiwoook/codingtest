import sys


def change_to_min(value):
    return int(value[:2]) * 60 + int(value[2:]) - (9 * 60)


def cnt_distance(v_time, idx, direction):
    count = 0
    step = 1 if direction == 0 else -1
    start = idx + step

    while 0 <= start < n:
        if time_table[v_time][start] == 1:
            return count
        count += 1
        start += step

    return count


def dispose(v_time):
    max_gap = -1
    best_idx = -1

    if sum(time_table[v_time]) == 0:
        return 0

    for i in range(n):
        if time_table[v_time][i] == 0:
            if i == 0:
                right = cnt_distance(v_time, i, 0)
                if max_gap < right:
                    max_gap = right
                    best_idx = i
            elif i == n - 1:
                left = cnt_distance(v_time, i, 1)
                if max_gap < left:
                    max_gap = left
                    best_idx = i
            else:
                left = cnt_distance(v_time, i, 1)
                right = cnt_distance(v_time, i, 0)
                if max_gap < min(right, left):
                    max_gap = min(right, left)
                    best_idx = i

    return best_idx


n, t, p = map(int, sys.stdin.readline().rstrip().split())
p -= 1
chair_list = [0 for _ in range(n)]
answer = 0
full_time = 12 * 60
time_table = [[0 for _ in range(n)] for _ in range(full_time + 1)]
time_list = sorted([list(map(change_to_min, sys.stdin.readline().rstrip().split())) for _ in range(t)])

for start_time, end_time in time_list:
    idx = dispose(start_time)
    for time in range(start_time, end_time):
        time_table[time][idx] = 1

answer = sum(time_table[time][p] == 0 for time in range(full_time))

print(answer)
