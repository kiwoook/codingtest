def cantor_set(s, start, end):
    if end - start <= 1:
        return

    third = (end - start) // 3

    for i in range(start + third, start + 2 * third):
        s[i] = ' '

    cantor_set(s, start, start + third)
    cantor_set(s, start + 2 * third, end)


while 1:
    try:
        n = int(input())
        length = 3 ** n
        s = ['-' for _ in range(length)]
        cantor_set(s, 0, length)

        print(''.join(s))

    except EOFError:
        break


