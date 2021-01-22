import random
from typing import List, Tuple
import cards

def card_value(card):
    
    numbers = "2345678910"
    letters = "JQKA"
    double_points = "♠♣"

    pontos = 0

    if card[1] in numbers:
        pontos = pontos + int(card[1])

    if card[1] in letters:
        pontos = pontos + 10

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
