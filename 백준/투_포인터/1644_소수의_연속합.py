def prime_list():
    sieve = [True] * 4000001
    primes = []

    for p in range(2, 4000001):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, 4000001, p):
                sieve[i] = False

    return primes


n = int(input())
answer = 0
prime_list = prime_list()

left, right = 0, 0

total = prime_list[0]
while left < len(prime_list) and right < len(prime_list):
    if total == n:
        answer += 1
        right += 1
        if right < len(prime_list):
            total += prime_list[right]

    if total < n:
        right += 1
        if right < len(prime_list):
            total += prime_list[right]

    if total > n and left < len(prime_list):
        total -= prime_list[left]
        left += 1

print(answer)
