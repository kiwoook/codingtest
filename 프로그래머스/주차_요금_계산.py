import math


def solution(fees, records):
    check_car = dict()
    fee_car = dict()
    sum_car = dict()

    for record in records:
        time, car, status = record.split(" ")
        sum_car[car] = 0

    for record in records:
        time, car, status = record.split(" ")
        hour, minute = map(int, time.split(":"))
        time = hour * 60 + minute
        if status == "IN":
            check_car[car] = time
        if status == 'OUT':
            total_time = time - check_car[car]
            check_car.pop(car)
            sum_car[car] += total_time

    for car, time in check_car.items():
        total_time = 23 * 60 + 59 - time
        sum_car[car] += total_time

    for car, total_time in sum_car.items():
        if total_time <= fees[0]:
            fee_car[car] = fees[1]
        else:
            fee_car[car] = fees[1] + (math.ceil((total_time - fees[0]) / fees[2]) * fees[3])

    return [fee_car[key] for key in sorted(fee_car.keys())]


print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
