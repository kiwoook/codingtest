min_cnt = 1e9


def dfs(move_cnt, idx, visited, count):
    global min_cnt

    if visited[idx] == 0:
        count += move_cnt[idx]
        visited[idx] = 1

    if all(visited):
        min_cnt = min(count, min_cnt)
        return

    left, right = idx, idx
    left_cnt, right_cnt = 0, 0

    while visited[left]:
        left_cnt += 1
        left = left - 1 if left - 1 >= 0 else len(move_cnt) - 1

    while visited[right]:
        right_cnt += 1
        right = right + 1 if right + 1 < len(move_cnt) else 0

    dfs(move_cnt, left, visited, count + left_cnt)
    visited[left] = 0

    dfs(move_cnt, right, visited, count + right_cnt)
    visited[right] = 0


def solution(name):
    move_cnt = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]

    visited = [0 for _ in range(len(name))]

    for i in range(len(name)):
        if name[i] == 'A':
            visited[i] = 1

    dfs(move_cnt, 0, visited, 0)

    return min_cnt


print(solution("AAABAAAA"))
