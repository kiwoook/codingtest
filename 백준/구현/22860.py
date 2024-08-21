import sys
from collections import defaultdict


def dfs(pos, path):
    global total_cnt_dict

    file_total_cnt, file_total_dict = 0, defaultdict(int)

    for name, flag in graph_dict[pos]:
        if flag == 1:
            path.append(pos)
            file_cnt, file_dict = dfs(name, path)
            path.pop()
            file_total_cnt += file_cnt
            file_total_dict.update(file_dict)
        else:
            file_total_cnt += 1
            file_total_dict[name] = 1

    folder_path = '/'.join(path) + "/" + pos if path else pos
    total_cnt_dict[folder_path] = [len(file_total_dict), file_total_cnt]

    return file_total_cnt, file_total_dict


n, m = map(int, sys.stdin.readline().rstrip().split())

total_cnt_dict, graph_dict = dict(), defaultdict(list)

for _ in range(n + m):
    p, f, c = sys.stdin.readline().rstrip().split()
    graph_dict[p].append((f, int(c)))

dfs('main', [])

q = int(sys.stdin.readline().rstrip())

for _ in range(q):
    print(*total_cnt_dict[sys.stdin.readline().rstrip()])
