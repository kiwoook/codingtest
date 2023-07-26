def solution(cacheSize, cities):
    time = 0
    cache = []

    for city in cities:
        city = city.lower()
        if city in cache:
            # hit
            time += 1
            cache.remove(city)
            cache.insert(0, city)
        else:
            # miss
            time += 5
            if cacheSize == 0:
                continue
            elif len(cache) >= cacheSize:
                cache.pop()
                cache.insert(0, city)
            else:
                cache.insert(0, city)

    return time


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
