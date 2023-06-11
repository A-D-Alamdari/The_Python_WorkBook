"""
Exercise 119: Dealing Hands of Cards

    In many card games each player is dealt a specific number of cards after the deck
    has been shuffled. Write a function, deal, which takes the number of hands, the
    number of cards per hand, and a deck of cards as its three parameters. Your function
    should return a list containing all of the hands that were dealt. Each hand will be
    represented as a list of cards.
    When dealing the hands, your function should modify the deck of cards passed
    to it as a parameter, removing each card from the deck as it is added to a player’s
    hand. When cards are dealt, it is customary to give each player a card before any
    player receives an additional card. Your function should follow this custom when
    constructing the hands for the players.
    Use your solution to Exercise 118 to help you construct a main program that
    creates and shuffles a deck of cards, and then deals out four hands of five cards each.
    Display all of the hands of cards, along with the cards remaining in the deck after
    the hands have been dealt.
"""

import random


def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    return deck


def shuffle_deck(deck):
    random.shuffle(deck)


def deal(num_hands, cards_per_hand, deck):
    hands = []
    for _ in range(num_hands):
        hand = []
        for _ in range(cards_per_hand):
            card = deck.pop()
            hand.append(card)
        hands.append(hand)
    return hands


def main():
    deck = create_deck()
    shuffle_deck(deck)

    num_hands = 4
    cards_per_hand = 5

    hands = deal(num_hands, cards_per_hand, deck)

    print("Hands:")
    for i, hand in enumerate(hands, start=1):
        print(f"Player {i}: {hand}")

    print("Cards remaining in the deck:", deck)


main()
