s = input()
print(1 if s == ''.join(list(s)[::-1]) else 0)
