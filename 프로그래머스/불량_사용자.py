set_table = set()


def check_user(user, id_filter):
    for idx, value in enumerate(id_filter):
        if value == '*':
            continue
        if user[idx] != value:
            return False
    return True


def is_visited(user, visited):
    for visit in visited:
        if user == visit:
            return True
    return False


def dfs(ban_list, depth, visited):

    if depth == len(ban_list):
        set_table.add(tuple(sorted(visited)))
        return

    for i in range(len(ban_list[depth])):
        if not is_visited(ban_list[depth][i], visited):
            visited.append(ban_list[depth][i])
            dfs(ban_list, depth + 1, visited)
            visited.remove(ban_list[depth][i])


def solution(user_id, banned_id):
    ban_selection = []

    for ban_id in banned_id:
        tmp_list = []
        for user in user_id:
            if len(ban_id) != len(user):
                continue
            if check_user(user, ban_id):
                tmp_list.append(user)
        ban_selection.append(tmp_list)

    dfs(ban_selection, 0, [])

    return len(set_table)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
