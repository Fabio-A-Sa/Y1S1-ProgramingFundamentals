# Created on January, 2021
# @author: Fábio Araújo de Sá

# Modules import
import random
from typing import List, Tuple

# card suits
SUITS = "♠ ♡ ♢ ♣".split()  # spade, heart, diamond, club
# card ranks
RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()  # 2-10, Jack, Queen, King, Ace

Card = Tuple[str, str]
Deck = List[Card]

def create_deck(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards"""
    deck = [(s, r) for r in RANKS for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into four hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def choose(items):
    """Choose and return a random item"""
    return random.choice(items)

def player_order(names, start=None):
    """Rotate player order so that start goes first"""
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

def card_value(card):
    
    numbers = ['2','3','4','5','6','7','8','9','10']
    letters = ['J','Q','K','A']
    double_points = ['♠','♣']

    pontos = 0

    if card[1] in numbers:
        pontos = pontos + int(card[1])

    if card[1] in letters and card[1] != 'A':
        pontos = pontos + 10

    if card[1] == 'A':
        pontos = pontos + 11

    if card[0] in double_points:
        pontos = pontos * 2
    
    return pontos

def play(seed) -> None:
    """Play a 4-player card game"""
    # Input seed from FPRO
    random.seed(seed)

    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, deal_hands(deck))}
    start_player = choose(names)
    turn_order = player_order(names, start=start_player)

    pontos = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}

    # Randomly play cards from each player's hand until empty
    while hands[start_player]:

        vencedor = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}
        
        for name in turn_order:
            card = choose(hands[name])
            # Add points
            vencedor[name] = vencedor[name] + card_value(card)
            hands[name].remove(card)

        maximo = vencedor[max(vencedor, key=vencedor.get)]

        alist = []
        for key, value in vencedor.items():
            if value == maximo:
                alist.append(key)

        for rei_da_rodada in alist:
            pontos[rei_da_rodada] = pontos[rei_da_rodada] + 1

    winners = []
    maximo_pontos = pontos[max(pontos, key=pontos.get)]
    for jogador, p in pontos.items():
        if p == maximo_pontos:
            winners.append(jogador)

    answer = ""
    for j in winners:
        answer = answer + j + " "

    return answer.strip()

seed = 98765432
print(play(seed))

# Another solution, with JCL's Module "cards"

# Import module from FPRO JCL
import cards
import random

def card_value(card):
    
    numbers = ['2','3','4','5','6','7','8','9','10']
    letters = ['J','Q','K','A']
    double_points = ['♠','♣']

    pontos = 0

    if card[1] in numbers:
        pontos = pontos + int(card[1])

    if card[1] in letters and card[1] != 'A':
        pontos = pontos + 10

    if card[1] == 'A':
        pontos = pontos + 11

    if card[0] in double_points:
        pontos = pontos * 2
    
    return pontos

def play(seed) -> None:
    """Play a 4-player card game"""
    # Input seed from FPRO
    random.seed(seed)

    deck = cards.create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h for n, h in zip(names, cards.deal_hands(deck))}
    start_player = cards.choose(names)
    turn_order = cards.player_order(names, start=start_player)

    pontos = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}

    # Randomly play cards from each player's hand until empty
    while hands[start_player]:

        vencedor = {'P1': 0, 'P2': 0, 'P3': 0, 'P4': 0}
        
        for name in turn_order:
            card = cards.choose(hands[name])
            # Add points
            vencedor[name] = vencedor[name] + card_value(card)
            hands[name].remove(card)

        maximo = vencedor[max(vencedor, key=vencedor.get)]

        alist = []
        for key, value in vencedor.items():
            if value == maximo:
                alist.append(key)

        for rei_da_rodada in alist:
            pontos[rei_da_rodada] = pontos[rei_da_rodada] + 1

    winners = []
    maximo_pontos = pontos[max(pontos, key=pontos.get)]
    for jogador, p in pontos.items():
        if p == maximo_pontos:
            winners.append(jogador)

    answer = ""
    for j in winners:
        answer = answer + j + " "

    return answer.strip()

seed = 98765432
print(play(seed))
