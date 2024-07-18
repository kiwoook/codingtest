n = int(input())
cnt = 1
answer = -1
answer_list = []


def dfs(number, last_digit):
    global cnt, answer, answer_list

    answer_list.append(number)

    for digit in range(last_digit):
        cnt += 1
        dfs(number * 10 + digit, digit)


for num in range(0, 10):
    dfs(num, num)
    cnt += 1

answer_list.sort()
if 0 <= n - 1 < len(answer_list):
    print(answer_list[n - 1])
else:
    print(-1)
