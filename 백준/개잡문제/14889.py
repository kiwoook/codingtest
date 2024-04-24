from itertools import combinations


def dfs(value_set, depth, previous_value, value):

    if depth == 2:
        return score[previous_value][value]

    hap = 0

    for v in value_set:
        if visited[v] == 0:
            visited[v] = 1
            hap += dfs(value_set, depth + 1, value, v)
            visited[v] = 0

    return hap


score = []
min_value = int(1e9)
n = int(input())

for _ in range(n):
    score.append(list(map(int, input().split())))

set_all = {i for i in range(n)}

set_n = set_all - {0}

comb_list = list(combinations(set_n, n // 2 - 1))

for comb in comb_list:
    start_team = set(comb)
    start_team.add(0)
    link_team = set_all - start_team
    visited = [0 for i in range(n)]
    diff1 = dfs(start_team, 0, -1, -1)
    diff2 = dfs(link_team, 0, -1, -1)
    min_value = min(min_value, abs(diff2 - diff1))

print(min_value)
