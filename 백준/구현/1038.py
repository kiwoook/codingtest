def down_num(value):
    global answer_list

    answer_list.append(int(value))

    for num in range(int(value[-1]) - 1, -1, -1):
        down_num(value + str(num))


n, answer_list = int(input()), []

for num in range(10):
    down_num(str(num))

answer_list.sort()

print(answer_list[n] if n < len(answer_list) else - 1)
