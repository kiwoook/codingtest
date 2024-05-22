k = int(input())
num_list = list(map(int, input().split()))

if k == 1:
    print(num_list[0] ** 2)
else:
    num_list.sort()
    print(num_list[0] * num_list[-1])
