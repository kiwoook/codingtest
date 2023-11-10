from itertools import product


def solution(users, emoticons):
    answer = []
    users_min_discount = []
    users_max_buy = []
    for discount, buy in users:
        users_min_discount.append(discount)
        users_max_buy.append(buy)

    emoticons_discount = list(product([10, 20, 30, 40], repeat=len(emoticons)))

    for discount in emoticons_discount:
        discount = list(discount)
        plus_buy = 0
        total_price = 0
        for i in range(len(users)):
            price = 0
            for idx, d in enumerate(discount):
                if users_min_discount[i] <= d:
                    price += int(emoticons[idx] * (100 - d) * 0.01)
            if price >= users_max_buy[i]:
                plus_buy += 1
            else:
                total_price += price
        answer.append([plus_buy, total_price])

    answer.sort(key=lambda x: (x[0], x[1]))

    return answer[-1]


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
