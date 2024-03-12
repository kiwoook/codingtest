import sys

dy = [0, 0, -1, 1, 0]
dx = [-1, 1, 0, 0, 0]


def switching(y, x):
    global tmp_board

    for n in range(5):
        ny = y + dy[n]
        nx = x + dx[n]
        if 0 <= ny < 10 and 0 <= nx < 10:
            if tmp_board[ny][nx] == 'O':
                tmp_board[ny][nx] = '#'
            elif tmp_board[ny][nx] == '#':
                tmp_board[ny][nx] = 'O'


board = []

for _ in range(10):
    tmp = sys.stdin.readline().rstrip()
    board.append(list(tmp))

answer = int(1e9)
tmp_board = [['0' for _ in range(10)] for _ in range(10)]
for number in range(2 ** 10):

    for i in range(10):
        for k in range(10):
            tmp_board[i][k] = board[i][k]
    # 1행에 대한 모든 경우의 수를 만든 다음 대입한 다음에 동작시킨다.
    sw = 1
    cnt = 0
    number = bin(number)[2:].zfill(10)
    for i in range(10):
        if number[i] == '1':
            switching(0, i)
            cnt += 1

    # 만약 내 위에거가 1이라면 지금 내꺼를
    for k in range(1, 10):
        for j in range(10):
            if tmp_board[k - 1][j] == 'O':
                switching(k, j)
                cnt += 1

    for k in range(10):
        if tmp_board[9][k] == 'O':
            # 모두 못끈거이므로 failed
            sw = 0
    if sw == 1:
        answer = min(answer, cnt)

if answer == int(1e9):
    print(-1)
else:
    print(answer)
