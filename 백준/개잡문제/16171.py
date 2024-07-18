s = input()
target = input()

filtered_s = ''

for char in s:
    if char.isalpha():
        filtered_s += char

if target in filtered_s:
    print(1)
else:
    print(0)
