n, k = map(int, input().split())
temp_list = list(map(int, input().split()))

sum_list = [sum(temp_list[:k])]

for idx, i in enumerate(range(k, n)):
    sum_list.append(sum_list[idx] - temp_list[idx] + temp_list[i])

print(max(sum_list))
