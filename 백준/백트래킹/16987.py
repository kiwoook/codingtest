import sys


def dfs(hand_idx):
    global answer, egg_info

    if hand_idx == n:
        cnt = sum(1 for d1, _ in egg_info if d1 <= 0)
        answer = max(answer, cnt)
        return

    if egg_info[hand_idx][0] <= 0:
        dfs(hand_idx + 1)
        return

    any_hit = False
    for idx in range(n):
        if idx != hand_idx and egg_info[idx][0] > 0:
            any_hit = True
            egg_info[hand_idx][0] -= egg_info[idx][1]
            egg_info[idx][0] -= egg_info[hand_idx][1]
            dfs(hand_idx + 1)
            egg_info[hand_idx][0] += egg_info[idx][1]
            egg_info[idx][0] += egg_info[hand_idx][1]

    if not any_hit:
        dfs(hand_idx + 1)


n = int(sys.stdin.readline().rstrip())
answer = 0
egg_info = []

for _ in range(n):
    d, w = map(int, sys.stdin.readline().rstrip().split())
    egg_info.append([d, w])

dfs(0)
print(answer)
