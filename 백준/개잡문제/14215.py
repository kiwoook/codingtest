a = sorted(list(map(int, input().split())))
print(2 * (a[0] + a[1]) - 1 if a[0] + a[1] <= a[2] else a[0] + a[1] + a[2])
