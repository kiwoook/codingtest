a1 = [1, 2, 3, 4, 5, 6]
b1 = [3, 3, 3, 3, 4, 4]

hap = set()

for i in a1:
    for k in b1:
        hap.add(i+k)

print(hap)