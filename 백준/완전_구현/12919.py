answer = 0


def dfs(string):
    global answer

    if len(s) == len(string):
        if s == string:
            answer = 1
        return

    if string[-1] == 'A':
        string.pop()
        dfs(string)
        string.append('A')
    if string[0] == 'B':
        string.reverse()
        string.pop()
        dfs(string)
        string.append('B')
        string.reverse()


s = list(input())
t = list(input())

dfs(t)
print(answer)
