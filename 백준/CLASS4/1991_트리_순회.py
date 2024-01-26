from collections import defaultdict

answer = ""


def post_order(pos):
    global answer
    if pos is None:
        return

    post_order(graph[pos][0])
    post_order(graph[pos][1])

    answer += pos


def inorder_recur(pos):
    global answer
    if pos is None:
        return

    inorder_recur(graph[pos][0])
    answer += pos
    inorder_recur(graph[pos][1])


def preorder_recur(pos):
    global answer
    if pos is None:
        return
    answer += pos
    preorder_recur(graph[pos][0])
    preorder_recur(graph[pos][1])


n = int(input())
graph = defaultdict(list)

for _ in range(n):
    a, b, c = input().split()
    if b == '.':
        b = None
    if c == '.':
        c = None
    graph[a] = [b, c]

preorder_recur('A')
print(answer)
answer = ""
inorder_recur('A')
print(answer)
answer = ""
post_order('A')
print(answer)
