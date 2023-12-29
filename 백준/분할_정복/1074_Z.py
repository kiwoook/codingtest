cnt = 0


def dfs(y, x, length):
    global cnt

    if length == 1:
        return

    if y== c and x == r:
        print(cnt)
        exit(0)

    # 시간 복잡도를 줄이기 위해
    # 필요한 부분만 연산해서 진입해야 한다.

    if y < c:
        pass

    if


n, r, c = map(int, input().split())

dfs(0, 0, n ** 2)
print(cnt)
