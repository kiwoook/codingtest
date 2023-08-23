path = []
min_cnt = 50


def DFS(pos, target, depth, graph):
    global min_cnt, path

    if pos == target:
        if min_cnt >= depth:
            min_cnt = depth
        return

    for i in range(len(graph)):
        if graph[pos][i] == 1:
            if path[i] == 0:
                depth += 1
                path[i] = 1
                DFS(i, target, depth, graph)
                path[i] = 0
                depth -= 1


def solution(begin, target, words):
    global path
    answer = 0
    words.insert(0, begin)
    len_words = len(words)
    len_word = len(words[0])
    path = [0] * len_words

    if target not in words:
        return 0

    # 간선 초기화
    graph = [[0] * len_words for _ in range(len_words)]
    # 간선 만들기
    for y, word_1 in enumerate(words):
        for x, word_2 in enumerate(words):
            change_cnt = 0
            for i in range(0, len_word):
                if word_1[i] != word_2[i]:
                    change_cnt += 1
            if change_cnt == 1:
                graph[y][x] = 1

    # DFS 탐색
    DFS(0, words.index(target), 0, graph)
    print(min_cnt)

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
