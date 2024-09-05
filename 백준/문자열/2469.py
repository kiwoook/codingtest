import sys

k = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
target_participants = list(sys.stdin.readline().rstrip())
participants = [chr(ord('A') + value) for value in range(k)]

quesiton_line = -1
line_list = []

for idx in range(n):
    v = sys.stdin.readline().rstrip()
    if v[0] == '?':
        quesiton_line = idx
    line_list.append(v)

for line_idx in range(quesiton_line):
    for idx, L in enumerate(line_list[line_idx]):
        if L == '-':
            participants[idx], participants[idx + 1] = participants[idx + 1], participants[idx]

for line_idx in range(n - 1, quesiton_line, -1):
    for idx, L in enumerate(line_list[line_idx]):
        if L == '-':
            target_participants[idx], target_participants[idx + 1] = target_participants[idx + 1], target_participants[
                idx]

result = []
idx = 0

while idx < k - 1:
    if participants[idx] == target_participants[idx]:
        result.append('*')
    elif idx + 1 < k and participants[idx + 1] == target_participants[idx] and participants[idx] == target_participants[
        idx + 1]:
        result.append('-')
        if idx != k - 2:
            result.append('*')
        idx += 1
    else:
        result = ['x'] * (k - 1)
        break
    idx += 1

print(''.join(result))
