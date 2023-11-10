def is_valid_move(park, x, y, dx, dy, n, m):
    if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m:
        return False

    if dx != 0:
        step_x = 1 if dx > 0 else -1
        for k in range(1, abs(dx) + 1):
            if park[y][x + step_x * k] == 'X':
                return False

    if dy != 0:
        step_y = 1 if dy > 0 else -1
        for k in range(1, abs(dy) + 1):
            if park[y + step_y * k][x] == 'X':
                return False

    return True


def solution(park, routes):
    n = len(park[0])
    m = len(park)
    x = -1
    y = -1

    for i in range(m):
        park[i] = list(park[i])
        if 'S' in park[i]:
            x = park[i].index('S')
            y = i

    for route in routes:
        dx = 0
        dy = 0
        if route[0] == 'E':
            dx = int(route[2])
        elif route[0] == 'W':
            dx = -int(route[2])
        elif route[0] == 'S':
            dy = int(route[2])
        elif route[0] == 'N':
            dy = -int(route[2])

        if not is_valid_move(park, x, y, dx, dy, n, m):
            continue

        park[y][x] = 'O'
        x += dx
        y += dy
        park[y][x] = 'S'

    for i in range(n):
        if 'S' in park[i]:
            x = park[i].index('S')
            y = i
            break

    return [y, x]


print(solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]))
