def recur(a, x_start, x_end, y_start, y_end):
    if x_end - x_start <= 1 or y_end - y_start <= 1:
        return

    x_third = (x_end - x_start) // 3
    y_third = (y_end - y_start) // 3

    for i in range(y_start + y_third, y_start + 2 * y_third):
        for k in range(x_start + x_third, x_start + 2 * x_third):
            a[i][k] = ' '

    recur(a, x_start, x_start + x_third, y_start, y_start + y_third)
    recur(a, x_start + 2 * x_third, x_end, y_start, y_start + y_third)
    recur(a, x_start, x_start + x_third, y_start + 2 * y_third, y_end)
    recur(a, x_start + 2 * x_third, x_end, y_start + 2 * y_third, y_end)


n = int(input())

arr = [['*' for _ in range(n)] for _ in range(n)]

recur(arr, 0, n, 0, n)

for a in arr:
    print(''.join(a))
