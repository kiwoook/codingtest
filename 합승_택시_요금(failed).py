visited_a = []
visited_b = []
min_a = 0
min_b = 0


def run_a(fare_map, now, n, cnt, destination):
    global min_a

    if now == destination:
        if cnt <= min_a:
            min_a = cnt
            print(min_a)
        return

    for i in range(1, n + 1):
        if fare_map[now][i] > 0 and visited_a[i] == 0:
            visited_a[i] = 1
            cnt += fare_map[now][i]
            run_a(fare_map, i, n, cnt, destination)
            cnt -= fare_map[now][i]
            visited_a[i] = 0


def solution(n, s, a, b, fares):
    global visited_a, visited_b, min_a, min_b
    answer = 0
    fare_map = [[0] * (n + 1) for _ in range(n + 1)]
    a_min_move = []
    b_min_move = []
    visited_a = [0] * (n + 1)
    visited_b = [0] * (n + 1)
    visited_a[s] = 1
    visited_b[s] = 1

    # 맵 만들기
    for fare in fares:
        fare_map[fare[0]][fare[1]] = fare[2]
        fare_map[fare[1]][fare[0]] = fare[2]

    min_a = min_b = sum(sum(row) for row in fare_map)

    print(fare_map)
    # a를 동작 시켜서 최소로 가는 데를 탐색.
    run_a(fare_map, s, n, 0, a)

    return answer


solution(6, 4, 6, 2,
         [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
