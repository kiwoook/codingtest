import sys


def add_result(arr):
    global result

    if len(arr) % 2 == 1:
        result.append(arr[-1])
        for i in range(0, len(arr) - 1, 2):
            if arr[i] + arr[i + 1] >= arr[i] * arr[i + 1]:
                result.append(arr[i] + arr[i + 1])
            else:
                result.append(arr[i] * arr[i + 1])
    else:
        for i in range(0, len(arr), 2):
            if arr[i] + arr[i + 1] >= arr[i] * arr[i + 1]:
                result.append(arr[i] + arr[i + 1])
            else:
                result.append(arr[i] * arr[i + 1])


n = int(sys.stdin.readline().rstrip())
num_list = []
positive_list = []
not_positive_list = []
for _ in range(n):
    num_list.append(int(sys.stdin.readline().rstrip()))

result = []
for num in num_list:
    if num <= 0:
        not_positive_list.append(num)
    else:
        positive_list.append(num)

positive_list.sort(reverse=True)
not_positive_list.sort()

add_result(positive_list)
add_result(not_positive_list)

print(sum(result))
