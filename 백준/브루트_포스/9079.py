import sys
from collections import deque


def bit_mask(tmp_value):
    return 0 if tmp_value == 'H' else 1


def board_to_value(tmp_board):
    flat_board = sum(tmp_board, [])
    return int(''.join(map(str, flat_board)), 2)


def change_row(tmp_value, idx):
    mask = (1 << (8 - idx * 3)) | (1 << (7 - idx * 3)) | (1 << (6 - idx * 3))
    return tmp_value ^ mask


def change_column(tmp_value, idx):
    mask = (1 << (8 - idx)) | (1 << (5 - idx)) | (1 << (2 - idx))
    return tmp_value ^ mask


def change_diagonal(tmp_value, flag):
    if flag == 0:
        mask = (1 << 8) | (1 << 4) | (1 << 0)
    else:
        mask = (1 << 6) | (1 << 4) | (1 << 2)
    return tmp_value ^ mask


T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    start = [list(map(bit_mask, sys.stdin.readline().rstrip().split())) for _ in range(3)]
    start_value = board_to_value(start)

    visited = {}
    q = deque([(start_value, 0)])
    answer = -1

    while q:
        value, cnt = q.popleft()

        if value == 0 or value == 2 ** 9 - 1:
            answer = cnt
            break

        if value not in visited:
            visited[value] = True

            for i in range(3):
                q.append((change_row(value, i), cnt + 1))
                q.append((change_column(value, i), cnt + 1))

            for i in range(2):
                q.append((change_diagonal(value, i), cnt + 1))

    print(answer)
