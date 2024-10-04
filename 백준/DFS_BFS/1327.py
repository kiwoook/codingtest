from collections import deque, defaultdict


def sort(v_list: list, idx: int):
    sorted_list = v_list[:]

    for i in range(k // 2):
        sorted_list[idx + i], sorted_list[idx + k - 1 - i] = sorted_list[idx + k - 1 - i], sorted_list[idx + i]

    return sorted_list


n, k = map(int, input().split())
num_list = list(map(int, input().split()))

target_num_list = sorted(num_list)

q = deque([(num_list, 0)])
visited = defaultdict(int)

while q:
    num_list, cnt = q.popleft()

    if num_list == target_num_list:
        print(cnt)
        exit(0)

    for idx in range(n - k + 1):
        v_list = sort(num_list, idx)
        if visited[tuple(v_list)] == 0:
            visited[tuple(v_list)] = 1
            q.append((v_list, cnt + 1))

print(-1)
