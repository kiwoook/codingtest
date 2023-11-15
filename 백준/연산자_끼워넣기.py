max_value = -int(1e9)
min_value = int(1e9)


def dfs(depth, branch, result, visited, operator_visited, number_list):
    global max_value, min_value
    if visited[branch] > operator_visited[branch]:
        return

    if branch == 0:
        result += number_list[depth]
    elif branch == 1:
        result -= number_list[depth]
    elif branch == 2:
        result *= number_list[depth]
    else:
        if result < 0:
            result = -result
            result //= number_list[depth]
            result = -result
        else:
            result //= number_list[depth]

    if depth == len(number_list) - 1:
        if result > max_value:
            max_value = result
        if result < min_value:
            min_value = result

    for k in range(4):
        visited[k] += 1
        dfs(depth + 1, k, result, visited, operator_visited, number_list)
        visited[k] -= 1


n = int(input())

num_list = list(map(int, input().split()))

operator_list = list(map(int, input().split()))
visited_list = [0, 0, 0, 0]

for i in range(4):
    visited_list[i] += 1
    dfs(1, i, num_list[0], visited_list, operator_list, num_list)
    visited_list[i] -= 1

print(max_value)
print(min_value)
