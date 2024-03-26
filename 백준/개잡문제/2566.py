import sys

max_value = - 1
board = []

for _ in range(9):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))

max_i = 0
max_k = 0
for i in range(9):
    for k in range(9):
        if board[i][k] > max_value:
            max_i = i
            max_k = k
            max_value = board[i][k]

print(max_value)
print(max_i+1, max_k+1)
