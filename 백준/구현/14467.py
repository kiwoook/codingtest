import sys

n = int(sys.stdin.readline().rstrip())
cow_dict = dict()
answer = 0

for _ in range(n):
    cow, pos = map(int, sys.stdin.readline().rstrip().split())

    if cow_dict.get(cow) is None:
        cow_dict[cow] = pos
    else:
        if cow_dict[cow] != pos:
            answer += 1
            cow_dict[cow] = pos

print(answer)
