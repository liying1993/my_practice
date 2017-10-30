rank = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}


def smallest_deck(): return min(len(p1_deck), len(p2_deck))


n = int(input())
p1_deck = [rank[input()[:-1]] for i in range(n)]
m = int(input())
p2_deck = [rank[input()[:-1]] for j in range(m)]

round = 0
while smallest_deck() > 0:
    round += 1
    compare = 0
    while (p1_deck[compare] == p2_deck[compare]):
        compare += 4
        if compare > smallest_deck(): print('PAT'); exit()
    if p1_deck[compare] > p2_deck[compare]:
        p1_deck = p1_deck[compare+1:] + p1_deck[:compare+1] + p2_deck[:compare+1]
        p2_deck = p2_deck[compare+1:]
    else:
        p2_deck = p2_deck[compare+1:]+p1_deck[:compare+1] + p2_deck[:compare+1]
        p1_deck = p1_deck[compare+1:]
winner = 1 if len(p2_deck) == 0 else 2
print(winner, round)
