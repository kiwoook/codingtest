def recur(a, x_start, x_end, y_start, y_end):
    if x_end - x_start <= 1 or y_end - y_start <= 1:
        return

    x_third = (x_end - x_start) // 3
    y_third = (y_end - y_start) // 3

    for i in range(y_start + y_third, y_start + 2 * y_third):
        for k in range(x_start + x_third, x_start + 2 * x_third):
            a[i][k] = ' '