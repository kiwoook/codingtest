def solution(players, callings):
    player_index = {player: idx for idx, player in enumerate(players)}

    for calling in callings:
        idx = player_index[calling]
        players[idx], players[idx - 1] = players[idx - 1], players[idx]
        player_index[players[idx]] = idx
        player_index[players[idx - 1]] = idx - 1

    return players


print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
