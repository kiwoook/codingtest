def next_permutation(value):
    value = list(value)
    i = len(value) - 2
    while i >= 0 and value[i] >= value[i + 1]:
        i -= 1
    if i == -1:
        return None

    j = len(value) - 1
    while value[j] <= value[i]:
        j -= 1

    value[i], value[j] = value[j], value[i]
    value[i + 1:] = reversed(value[i + 1:])

    return ''.join(value)


t = int(input())
for _ in range(t):
    s = input()
    result = next_permutation(s)
    print(result if result else s)