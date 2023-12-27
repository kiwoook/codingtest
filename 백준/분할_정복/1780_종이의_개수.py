import sys

one = 0
two = 0
three = 0


def check(start_y, start_x, length):
    sw = True
    # 1인지 체크
    for a in range(start_y, start_y + length):
        for b in range(start_x, start_x + length):
            if board[a][b] != 1:
                sw = False
                break
        if not sw:
            break
    if sw:
        return 1

    sw = True

    # 0인지 체크
    for a in range(start_y, start_y + length):
        for b in range(start_x, start_x + length):
            if board[a][b] != 0:
                sw = False
                break
        if not sw:
            break
    if sw:
        return 0

    sw = True

    for a in range(start_y, start_y + length):
        for b in range(start_x, start_x + length):
            if board[a][b] != -1:
                sw = False
                break
        if not sw:
            break
    if sw:
        return -1

    return -2


def recur(start_y, start_x, length):
    global one, two, three

    if length == 0:
        return

    value = check(start_y, start_x, length)

    if value == -2:
        recur(start_y, start_x, length // 3)
        recur(start_y, start_x + length // 3, length // 3)
        recur(start_y, start_x + 2 * (length // 3), length // 3)
        recur(start_y + length // 3, start_x, length // 3)
        recur(start_y + length // 3, start_x + length // 3, length // 3)
        recur(start_y + length // 3, start_x + 2 * (length // 3), length // 3)
        recur(start_y + 2 * (length // 3), start_x, length // 3)
        recur(start_y + 2 * (length // 3), start_x + length // 3, length // 3)
        recur(start_y + 2 * (length // 3), start_x + 2 * (length // 3), length // 3)

    if value == -1:
        one += 1
        return
    if value == 0:
        two += 1
        return
    if value == 1:
        three += 1


board = []

n = int(input())

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

recur(0, 0, n)

print(one)
print(two)
print(three)
