s = input()

checking = list('quack')
start_idx_list = []

for idx, char in enumerate(s):
    if char == 'q':
        start_idx_list.append(idx)

visited = [0 for _ in range(len(s))]
answer = 0
cnt = 0
for start_idx in start_idx_list:
    sw = 0
    check_idx = 0
    for idx in range(start_idx, len(s)):
        if visited[idx] == 0 and s[idx] == checking[check_idx]:
            visited[idx] = 1
            check_idx += 1
            if check_idx == len(checking):
                check_idx = 0
                sw = 1
                cnt += 1
    if sw == 1:
        answer += 1

if cnt != len(start_idx_list) or all(visited) != 1:
    print(-1)
else:
    print(answer)
