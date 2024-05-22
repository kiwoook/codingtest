import sys

n = int(sys.stdin.readline().rstrip())

visited_dict = dict()
answer = 0
for _ in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd == 'ENTER':
        visited_dict.clear()
    else:
        if visited_dict.get(cmd) is None:
            answer += 1
            visited_dict[cmd] = 1

print(answer)
