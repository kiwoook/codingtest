def solution(wallpaper):
    n = len(wallpaper)
    m = len(wallpaper[0])
    left, top = 1e9, 1e9
    right, bottom = 0, 0

    for y in range(n):
        for x in range(m):
            if wallpaper[y][x] == '#':
                if left >= x:
                    left = x
                if top >= y:
                    top = y
                if right <= x:
                    right = x
                if bottom <= y:
                    bottom = y

    return [top, left, bottom+1, right+1]


print(solution([".#...", "..#..", "...#."]))
print(solution(["..........", ".....#....", "......##..", "...##.....", "....#....."]))
