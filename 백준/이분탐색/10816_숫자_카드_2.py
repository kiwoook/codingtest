from collections import Counter


def binary_search(number_list, find_num):
    start, end = 0, len(number_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if number_list[mid] == find_num:
            return str(num_count_dict[num_list[mid]])
        if number_list[mid] < find_num:
            start = mid + 1
        if number_list[mid] > find_num:
            end = mid - 1

    return "0"


n = int(input())

num_list = list(map(int, input().split()))
num_count_dict = dict(Counter(num_list))

num_list.sort()

m = int(input())

find_list = list(map(int, input().split()))

answer = []

for num in find_list:
    answer.append(binary_search(num_list, num))

print(' '.join(answer))
