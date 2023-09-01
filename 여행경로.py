n = 0
path = []
sw = 0


def dfs(pos, ticket_used, visited, tickets_to_num, history):
    global path, sw
    if sw == 1:
        return
    if all(ticket_used) and all(visited):
        path.append(history.copy())
        sw = 1
        return

    for i in range(n):
        if tickets_to_num[i][0] == pos:
            if not ticket_used[i]:
                ticket_used[i] = True
                visited[tickets_to_num[i][1]] = True
                history.append(tickets_to_num[i][1])
                dfs(tickets_to_num[i][1], ticket_used, visited, tickets_to_num, history)
                history.pop()
                visited[tickets_to_num[i][1]] = False
                ticket_used[i] = False


def solution(tickets):
    global n, path
    airport = sorted(set(sum(tickets, [])))
    n = len(tickets)
    airport_len = len(airport)
    position_dict = dict()
    tickets_to_num = []
    answer = []
    visited = [False for _ in range(airport_len)]
    ticket_used = [False for _ in range(n)]
    for idx, i in enumerate(airport):
        position_dict[i] = idx

    start_idx = position_dict['ICN']
    tickets.sort(key=lambda x: x[1])
    for ticket in tickets:
        tickets_to_num.append([position_dict[ticket[0]], position_dict[ticket[1]]])

    visited[start_idx] = True
    dfs(start_idx, ticket_used, visited, tickets_to_num, [start_idx])
    for p in path[0]:
        answer.append(airport[p])

    return answer


