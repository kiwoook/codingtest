def solution(n, words):
    used = []
    previous = ""
    for idx, word in enumerate(words):
        if idx >= 1 and previous[-1] != word[0]:
            return [idx % n + 1, idx // n + 1]
        else:
            if word in used:
                return [idx % n + 1, idx // n + 1]
            else:
                used.append(word)
                previous = word

    return [0,0]