a = list(map(int, input().split()))

ascend_a = sorted(a)

if a == ascend_a:
    print("ascending")
elif a == ascend_a[::-1]:
    print("descending")
else:
    print("mixed")