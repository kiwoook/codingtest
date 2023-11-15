stack = []

expression = '()[[]]{([])}'
sw = 0
for e in expression:
    if e == '(' or e == '[':
        stack.append(e)
    elif e == ')' or e == ']':
        if e == ']':
            if '[' not in stack:
                sw = 1
                break
        if e == ')':
            if '(' not in stack:
                sw = 1
                break
        value = 0
        while stack:
            s = stack.pop()
            if s == '(':
                if value == 0:
                    value = 2
                else:
                    value *= 2
                break
            elif s == '[':
                if value == 0:
                    value = 3
                else:
                    value *= 3
                break
            else:
                value += int(s)
        stack.append(str(value))
    else:
        stack.append(e)

if '[' in stack or ']' in stack or '(' in stack or ')' in stack or sw:
    print(0)
else:
    print(sum(map(int, stack)))
