def solution(phone_book):
    table = dict()

    for phone in phone_book:
        table[phone] = True

    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[0:i] in table:
                return False

    return True


print(solution(["123", "1005", "1006", "1007"]))
