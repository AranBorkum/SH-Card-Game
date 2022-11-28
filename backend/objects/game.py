from typing import List
from objects.player import Player
from objects.cards import Deck


class Game:
    def __init__(self, n_players: int):
        self.deck = Deck().deck
        self.n_players: int = n_players
        self.players: List[Player] = [self.make_player() for _ in range(self.n_players)]

    def make_player(self):
        input_for_player = [self.deck.pop() for _ in range(9)]
        return Player(initial_cards_dealt=input_for_player)

    def player_setup(self):
        for player_n in self.players:
            player_n.choose_face_up_cards()


if __name__ == "__main__":
    game = Game(2)
    for index, player in enumerate(game.players):
        print(f"Player {index+1}")
        player.show_face_down_vards()
