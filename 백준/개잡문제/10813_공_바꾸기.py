n, m = map(int, input().split())

ball_list = [i for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    ball_list[a], ball_list[b] = ball_list[b], ball_list[a]

print(*ball_list[1:n+1])