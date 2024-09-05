for _ in range(3):
    time1, time2 = input().split()
    answer = 0

    hour1, min1, sec1 = map(int, time1.split(":"))
    total1 = hour1 * 3600 + min1 * 60 + sec1

    hour2, min2, sec2 = map(int, time2.split(":"))
    total2 = hour2 * 3600 + min2 * 60 + sec2

    if total1 > total2:
        total2 += 60 * 60 * 24

    for time in range(total1, total2 + 1):
        if time >= 60 * 60 * 24:
            time -= 60 * 60 * 24

        hour = time // (60 * 60)
        minute = (time % 3600) // 60
        sec = time % 60

        answer += 1 if int(str(hour) + str(minute) + str(sec)) % 3 == 0 else 0

    print(answer)
