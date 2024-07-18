n, m = map(int, input().split())
a = list(map(int, input().split()))

prefix_sum = [0] * n
prefix_sum[0] = a[0]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + a[i]

answer = 0

mod_count = {}

for sum_val in prefix_sum:
    mod_val = sum_val % m

    if mod_val == 0:
        answer += 1

    if mod_val in mod_count:
        answer += mod_count[mod_val]
        mod_count[mod_val] += 1
    else:
        mod_count[mod_val] = 1

print(answer)
