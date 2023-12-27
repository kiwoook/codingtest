s = ""


def check(start_y, start_x, length):
    cnt = 0
    for a in range(start_y, start_y + length):
        for b in range(start_x, start_x + length):
            cnt += board[a][b]

    if cnt == length ** 2:
        return 1
    elif cnt == 0:
        return 0
    else:
        return -1


def recur(start_y, start_x, length):
    global s

    if length == 0:
        return

    value = check(start_y, start_x, length)

    if value == -1:
        s += '('
        recur(start_y, start_x, length // 2)
        recur(start_y, start_x + length // 2, length // 2)
        recur(start_y + length // 2, start_x, length // 2)
        recur(start_y + length // 2, start_x + length // 2, length // 2)
        s += ')'
    if value == 0:
        s += '0'
    if value == 1:
        s += '1'


n = int(input())
board = []

for i in range(n):
    board.append(list(map(int, list(input()))))

recur(0, 0, n)

print(s)
