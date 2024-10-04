num_list = list(map(int, input().split()))
target_list = [1, 2, 3, 4, 5]

while num_list != target_list:
    for i in range(4):
        if num_list[i] > num_list[i + 1]:
            num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
            print(*num_list)

