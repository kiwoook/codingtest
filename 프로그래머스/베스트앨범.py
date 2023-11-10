def solution(genres, plays):
    answer = []
    genres_dict = dict()
    music_dict = dict()

    id_dict = dict()
    for i in range(len(genres)):
        id_dict[i] = plays[i]

    id_dict = dict(sorted(id_dict.items(), key=lambda x: x[1], reverse=True))

    for i in id_dict.keys():
        genre = genres[i]
        if genre in music_dict:
            music_dict[genre][i] = id_dict[i]
        else:
            music_dict[genre] = dict()
            music_dict[genre][i] = id_dict[i]

    for idx in range(len(genres)):
        if genres[idx] in genres_dict:
            genres_dict[genres[idx]] += plays[idx]
        else:
            genres_dict[genres[idx]] = 0
            genres_dict[genres[idx]] += plays[idx]

    genres_dict = dict(sorted(genres_dict.items(), key=lambda x: x[1], reverse=True))

    for key in genres_dict.keys():
        limit = 0
        cnt = 0
        if len(music_dict[key]) == 1:
            limit = 1
        else:
            limit = 2
        for a in music_dict[key].keys():
            if cnt == limit:
                break
            cnt += 1
            answer.append(a)

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
