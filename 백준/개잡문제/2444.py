n = int(input())

print_list = [None]
for i in range(1, 2 * n):
    if i <= n:
        print_list.append([' '] * (n - i) + ['*'] * (2 * i - 1))
    else:
        print_list.append(print_list[2 * n - i])

for i in range(1, len(print_list)):
    for value in print_list[i]:
        print(value, end='')
    print()
