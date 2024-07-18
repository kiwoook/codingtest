import sys

n = int(sys.stdin.readline().rstrip())

answer = 0

rope_list = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)], reverse=True)

for idx, rope in enumerate(rope_list):
    answer = max(answer, rope * (idx + 1))

print(answer)
