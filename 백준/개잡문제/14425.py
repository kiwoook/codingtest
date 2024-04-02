import sys

string_dict = dict()

n, m = map(int, sys.stdin.readline().rstrip().split())

for _ in range(n):
    s = sys.stdin.readline().rstrip()
    string_dict[s] = 1

answer = 0

for _ in range(m):
    s = sys.stdin.readline().rstrip()
    if string_dict.get(s) is not None:
        answer += 1

print(answer)
