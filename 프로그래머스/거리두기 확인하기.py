dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
sw = 0


def dfs(place, n, y, x, cnt):
    global dy, dx, sw
    if sw:
        return

    if cnt > 2:
        return

    if cnt != 0 and place[y][x] == 'P':
        sw = 1
        return

    for i in range(4):
        if 0 <= y + dy[i] < n and 0 <= x + dx[i] < n:
            if place[y + dy[i]][x + dx[i]] != 'X':
                place[y][x] = 'Z'
                dfs(place, n, y+dy[i], x+dx[i], cnt + 1)
                place[y][x] = 'O'

def check_p(place):
    global sw
    n = len(place)
    sw = 0
    for y in range(n):
        for x in range(n):
            if place[y][x] == 'P':

                dfs(place, n, y, x, 0)
        if sw == 1:
            return 0

    return 1


def solution(places):
    answer = []

    for place in places:
        for idx, value in enumerate(place):
            place[idx] = list(value)

    for place in places:
        answer.append(check_p(place))

    return answer

#
# print(solution([["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"]]))

print(solution(([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                 ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                 ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])))
