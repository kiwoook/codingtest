answer = set()


def dfs(expression, depth, history):
    global answer
    if depth == len(expression):
        if len(history) == 0:
            answer.add(''.join(expression))
        return

    if expression[depth] == '(':
        expression[depth] = ''
        history.append('')
        dfs(expression, depth + 1, history)
        history.pop()
        expression[depth] = original_exp[depth]

        history.append('(')
        dfs(expression, depth + 1, history)
        history.pop()

    elif expression[depth] == ')':
        if history and history[-1] == '':
            expression[depth] = ''
            history.pop()
            dfs(expression, depth + 1, history)
            history.append('')
            expression[depth] = original_exp[depth]
        if history and history[-1] == '(':
            history.pop()
            dfs(expression, depth + 1, history)
            history.append('(')

    else:
        dfs(expression, depth + 1, history)


exp = list(input())
original_exp = exp[:]

dfs(exp, 0, [])
answer = sorted(answer)

for ans in answer[1:]:
    print(ans)
