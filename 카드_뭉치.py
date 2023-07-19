
def solution(cards1, cards2, goal):
    cards1_list = []
    cards2_list = []
    for card1 in cards1:
        if card1 in goal:
            cards1_list.append(goal.index(card1))
        else:
            cards1_list.append(21)
    for card2 in cards2:
        if card2 in goal:
            cards2_list.append(goal.index(card2))
        else:
            cards2_list.append(21)

    if cards1_list == sorted(cards1_list) and cards2_list == sorted(cards2_list):
        return "Yes"
    else :
        return "No"




