import sys

paper = [[0 for _ in range(100)] for _ in range(101)]

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    y, x = map(int, sys.stdin.readline().rstrip().split())
    for i in range(y, y+10):
        for k in range(x, x+10):
            paper[i][k] = 1

answer = 0
for i in range(100):
    for k in range(100):
        if paper[i][k] == 1:
            answer += 1

print(answer)