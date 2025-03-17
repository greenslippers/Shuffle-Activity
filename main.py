from random import randint

CARDS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["♥", "♦", "♠", "♣"]


deck_of_cards = [f"{card}{suit}" for card in CARDS for suit in SUITS]
print("Initial deck:", deck_of_cards)

# Implement a solution for shuffling a deck of cards
# Use only randint() and no other imports
def shuffle_deck(deck_of_cards):
    shuffled_deck = []
    for _ in range(len(deck_of_cards)):
        index = randint(0, len(deck_of_cards) - 1)
        shuffled_deck.append(deck_of_cards.pop(index))

    return shuffled_deck

shuffled_deck = shuffle_deck(deck_of_cards)
print("Shuffled deck:", shuffled_deck)
