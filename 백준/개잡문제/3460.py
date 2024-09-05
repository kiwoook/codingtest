import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    answer = []
    v = bin(int(sys.stdin.readline().rstrip()))
    for idx, char in enumerate(v[:1:-1]):
        if char == '1':
            answer.append(idx)

    print(*answer)
