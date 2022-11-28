from random import shuffle
from dataclasses import dataclass
from typing import List
from enum import Enum, auto

VALUES: List[str] = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUITES: List[str] = ["S", "H", "C", "D"]


class CardValues(Enum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class CardSuites(Enum):
    SPADES = auto()
    HEARTS = auto()
    CLUBS = auto()
    DIAMONDS = auto()


@dataclass
class Card:
    def __init__(self, value: CardValues, suite: CardSuites):
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
        for suite in CardSuites:
            for value in CardValues:
                self.deck.append(Card(value, suite))

    def shuffle_deck(self):
        shuffle(self.deck)


if __name__ == "__main__":
    print([i for i in CardSuites])
    print([i.name for i in CardValues])
