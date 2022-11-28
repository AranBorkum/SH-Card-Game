from random import shuffle
from dataclasses import dataclass
from typing import List

VALUES: List[str] = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUITES: List[str] = ["S", "H", "C", "D"]


@dataclass
class Card:
    def __init__(self, value: str, suite: str):
        self.id = "".join([value, suite])
        self.suite = suite
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suite}"


class Deck:
    deck: List[Card] = []

    def __init__(self):
        self.initialise_deck()
        self.shuffle_deck()

    def initialise_deck(self):
        for suite in SUITES:
            for value in VALUES:
                self.deck.append(Card(value, suite))

    def shuffle_deck(self):
        shuffle(self.deck)
