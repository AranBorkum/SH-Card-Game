from typing import List
from objects.cards import Card, Deck


class Player:
    face_down_cards: List[Card] = []
    face_up_cards: List[Card] = []
    cards_in_hand: List[Card] = []
    temp_cards_in_hand: List[Card] = []

    def __init__(self, initial_cards_dealt: List[Card]):
        self.face_down_cards = initial_cards_dealt[:3]
        self.temp_cards_in_hand = initial_cards_dealt[3:]

    def choose_face_up_cards(self):
        print([card.id for card in self.temp_cards_in_hand])
        card_indices = []
        for i in range(3):
            card_indices.append(int(input(f"Card number {i+1}: ")))
        card_indices.sort(reverse=True)
        for i in card_indices:
            self.face_up_cards.append(self.temp_cards_in_hand.pop(i - 1))
        self.cards_in_hand = self.temp_cards_in_hand
        self.temp_cards_in_hand = []

    def show_hand(self):
        for card in self.cards_in_hand:
            print(card)

    def show_face_up_cards(self):
        for card in self.face_up_cards:
            print(card)

    def show_face_down_vards(self):
        for card in self.face_down_cards:
            print(card)


if __name__ == "__main__":
    deck = Deck()
    player = Player(deck.deck[:9])
    player.choose_face_up_cards()
    player.show_face_up_cards()
    player.show_hand()
