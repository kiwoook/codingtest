s = input()

key_dict = dict()
for i in range(len(s)):
    for k in range(i, len(s)):
        key_dict[s[i:k+1]] = 1

print(len(key_dict))
