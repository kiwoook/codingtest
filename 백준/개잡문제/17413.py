from collections import deque

s = input() + ' '

q = deque([])
result = ''

sw = 1
for char in s:
    if char == '<':
        while q:
            result += q.pop()
        sw = 0
        q.append(char)

    elif char == '>':
        q.append(char)
        while q:
            result += q.popleft()
        sw = 1

    elif char == ' ':
        if sw == 0:
            while q:
                result += q.popleft()
        if sw == 1:
            while q:
                result += q.pop()
        result += ' '
    else:
        q.append(char)

print(result)
