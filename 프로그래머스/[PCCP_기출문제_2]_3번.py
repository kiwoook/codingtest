from collections import defaultdict


def solution(points, routes):
    answer = 0

    n, m = -1, -1
    for y, x in points:
        n, m = max(n, y), max(m, x)

    visited = [[[0 for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(len(routes))]

    for idx, route in enumerate(routes):
        point = route[0]
        start_y, start_x = points[point - 1]
        target_list = route[1:]
        cnt = 1
        visited[idx][start_y][start_x] = cnt
        for target_point in target_list:
            target_y, target_x = points[target_point - 1]

            while start_y != target_y or start_x != target_x:
                if start_y < target_y:
                    start_y += 1
                elif start_y > target_y:
                    start_y -= 1
                elif start_x < target_x:
                    start_x += 1
                elif start_x > target_x:
                    start_x -= 1
                cnt += 1
                visited[idx][start_y][start_x] = cnt

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cnt_dict = defaultdict(int)
            for point in range(len(routes)):
                if visited[point][i][j] != 0:
                    cnt_dict[visited[point][i][j]] += 1
                    if cnt_dict[visited[point][i][j]] >= 2:
                        answer += 1
                        break

    return answer


print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [2, 4]]))
print(solution([[3, 2], [6, 4], [4, 7], [1, 4]], [[4, 2], [1, 3], [4, 2], [4, 3]]))
print(solution([[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]], [[2, 3, 4, 5], [1, 3, 4, 5]]
               ))
