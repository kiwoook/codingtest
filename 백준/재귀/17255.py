def recur(depth, trace, left, right, value):
    global answer_set
    if depth == len(s) - 1:
        answer_set.add(tuple(trace))
        return

    if left < 0:
        # 오른쪽 밖에 못감
        value += s[right]
        trace.append(value)
        recur(depth + 1, trace, left, right + 1, value)
        trace.pop()
    elif right > len(s) - 1:
        # 왼쪽밖에 못감
        value = s[left] + value
        trace.append(value)
        recur(depth + 1, trace, left - 1, right, value)
        trace.pop()
    else:
        v_right = value + s[right]
        trace.append(v_right)
        recur(depth + 1, trace, left, right + 1, v_right)
        trace.pop()
        v_left = s[left] + value
        trace.append(v_left)
        recur(depth + 1, trace, left - 1, right, v_left)
        trace.pop()


answer_set = set()
s = input()

for i in range(len(s)):
    recur(0, [s[i]], i - 1, i + 1, s[i])

print(len(answer_set))
