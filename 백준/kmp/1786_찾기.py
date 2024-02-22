def get_pi(s):
    pi = [0 for _ in range(len(s))]

    i = 0

    for j in range(1, len(s)):
        while i > 0 and s[i] != s[j]:
            i = pi[i - 1]

        if s[i] == s[j]:
            i += 1
            pi[j] = i

    return pi


def kmp(s, p):
    pi = get_pi(p)

    result = []
    i = 0
    for j in range(len(s)):
        while i > 0 and p[i] != s[j]:
            i = pi[i - 1]

        if p[i] == s[j]:
            i += 1
            if i == len(p):
                result.append(j - i + 2)
                i = pi[i - 1]

    return result

t = input()
p = input()
a = kmp(t, p)

print(len(a))
print(*a)
