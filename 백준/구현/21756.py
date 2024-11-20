n = int(input())

num_list = [i for i in range(1, n + 1)]

while len(num_list) != 1:
    tmp_list = []
    for idx, value in enumerate(num_list):
        if idx % 2 == 1:
            tmp_list.append(value)
    num_list = tmp_list

print(num_list[0])
