t = int(input())
for _ in range(t):
    n = int(input())
    dp = [[0 for _ in range(n)] for _ in range(2)]
    a = []
    for _ in range(n):
        a.append(list(map(int, input())))


