suits = 'shdc'  # Spades, Hearts, Diamonds, Clubs
ranks = list('23456789') + ['10', 'J', 'Q', 'K', 'A']
rank_order = {
    '2':1,
    '3':2,
    '4':3,
    '5':4,
    '6':5,
    '7':6,
    '8':7,
    '9':8,
    '10':9,
    'J':10,
    'Q':11,
    'K':12,
    'A':13

}

def create_deck(suits, ranks, reverse=False):
    deck = [
        [
            r + s
            for r in sorted(ranks, key=lambda rank: rank_order[rank], reverse=reverse)
        ]
        for s in suits
    ]

    return deck

print(create_deck(suits, ranks))
print(create_deck(suits, ranks, reverse=True))




