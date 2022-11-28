from objects.game import Game
from objects.cards import Card, CardValues


class CardFunctions:
    def __init__(self, game: Game):
        self.game = game

    def can_play_card(self, card: Card):
        if (
            card.value == CardValues.TWO
            or card.value == CardValues.EIGHT
            or card.value == CardValues.TEN
        ):
            return True

        if (
            card.value == CardValues.THREE
            or card.value == CardValues.FOUR
            or card.value == CardValues.FIVE
            or card.value == CardValues.SIX
            or card.value == CardValues.SEVEN
        ):
            if (
                self.game.deck[-1].value.value <= card.value.value
                or self.game.deck[-1].value == CardValues.SEVEN
            ):
                return True
            else:
                return False

        if (
            card.value == CardValues.JACK
            or card.value == CardValues.QUEEN
            or card.value == CardValues.KING
            or card.value == CardValues.ACE
        ):
            if self.game.deck[-1].value.value <= card.value.value:
                return True
            else:
                return False

    def magic_function(self, card: Card):
        if card.value == CardValues.TEN:
            self.game.draw_pile = []
        if card.value == CardValues.EIGHT:
            self.game.acting_top_card = self.game.draw_pile[-2]
