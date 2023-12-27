def binary_search(number_list, find_num):
    start, end = 0, len(number_list) - 1

    while start <= end:
        mid = (start + end) // 2

        if number_list[mid] == find_num:
            return 1
        if number_list[mid] < find_num:
            start = mid + 1
        if number_list[mid] > find_num:
            end = mid - 1

    return 0


n = int(input())

num_list = list(map(int, input().split()))

num_list.sort()

m = int(input())

find_list = list(map(int, input().split()))

for num in find_list:
    print(binary_search(num_list, num))
