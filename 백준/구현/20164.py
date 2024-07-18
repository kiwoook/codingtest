max_answer = 0
min_answer = 10 ** 9


def count_odds(num_list):
    return sum(1 for num in num_list if int(num) % 2 == 1)


def dfs(num_list, cnt):
    global max_answer, min_answer
    cnt += count_odds(num_list)

    if len(num_list) == 1:
        max_answer = max(max_answer, cnt)
        min_answer = min(min_answer, cnt)
        return

    elif len(num_list) == 2:
        num_list = list(str(int(num_list[0]) + int(num_list[1])))
        dfs(num_list, cnt)
        return

    else:
        for i in range(len(num_list) - 2):
            for k in range(i + 1, len(num_list) - 1):
                num1 = int(''.join(num_list[:i + 1]))
                num2 = int(''.join(num_list[i + 1:k + 1]))
                num3 = int(''.join(num_list[k + 1:]))
                new_num = str(num1 + num2 + num3)
                dfs(list(new_num), cnt)


n = list(input())
dfs(n, 0)
print(min_answer, max_answer)
