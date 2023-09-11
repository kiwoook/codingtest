from collections import defaultdict, Counter


def checking(fruit_cnt, want_cnt):
    sw = 0
    for k, v in fruit_cnt.items():
        if k in want_cnt and want_cnt[k] > v:
            sw = 1
            break
    if not sw:
        return True
    return False


def solution(want, number, discount):
    answer = 0
    discount_len = len(discount)
    fruit_cnt = defaultdict(int)
    want_cnt = dict()

    if not (set(want) < set(discount)):
        return 0

    for idx, num in enumerate(number):
        want_cnt[want[idx]] = num

    for i in range(10):
        fruit_cnt[discount[i]] += 1

    answer += 1 if checking(fruit_cnt, want_cnt) else 0

    for i in range(discount_len - 10):
        fruit_cnt[discount[i]] -= 1
        fruit_cnt[discount[i + 10]] += 1
        answer += 1 if checking(fruit_cnt, want_cnt) else 0
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                "banana", "apple", "banana"]))
