s = input()

for i in range(0, len(s), 10):
    print(s[i:min((i + 10), len(s))])
