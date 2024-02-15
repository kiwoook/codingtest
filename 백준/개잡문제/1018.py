import sys


def checking_board(y, x):
    tmp_answer = []
    cnt = 0

    for i in range(y, y + 8):
        if i % 2 == 0:
            for k in range(x, x + 8):
                if k % 2 == 0 and board[i][k] != 'W':
                    cnt += 1
                if k % 2 == 1 and board[i][k] != 'B':
                    cnt += 1

        if i % 2 == 1:
            for k in range(x, x + 8):
                if k % 2 == 0 and board[i][k] != 'B':
                    cnt += 1
                if k % 2 == 1 and board[i][k] != 'W':
                    cnt += 1

    tmp_answer.append(cnt)
    cnt = 0

    for i in range(y, y + 8):
        if i % 2 == 1:
            for k in range(x, x + 8):
                if k % 2 == 0 and board[i][k] != 'W':
                    cnt += 1
                if k % 2 == 1 and board[i][k] != 'B':
                    cnt += 1

        if i % 2 == 0:
            for k in range(x, x + 8):
                if k % 2 == 0 and board[i][k] != 'B':
                    cnt += 1
                if k % 2 == 1 and board[i][k] != 'W':
                    cnt += 1

    tmp_answer.append(cnt)

    return min(tmp_answer)


board = []
answer = []

m, n = map(int, sys.stdin.readline().rstrip().split())

for _ in range(m):
    board.append(list(sys.stdin.readline().rstrip()))

for y in range(m - 7):
    for x in range(n - 7):
        answer.append(checking_board(y, x))

print(min(answer))
