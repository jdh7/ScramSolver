#!/usr/bin/python3
from __future__ import annotations
from typing import Iterator, List, Tuple, Generic, TypeVar, NamedTuple, Union
import pdb
import time
from card_shower import Show_board


T = TypeVar("T")


class Board(object):
    top: int = 0
    right: int = 1
    bot: int = 2
    left: int = 3

    Card: Generic[T]
    available_cards: List[Card]
    used_cards: List[Card]
    board: List[Card]
    visited: List[str]

    def __init__(self, board=None, used_cards=[]) -> None:
        self.board = board
        self.used_cards = used_cards

    def clear_board(self) -> None:
        self.board = [None for _ in range(9)]

    def get_board(self, a: int = None) -> List[Card]:
        if a == None:
            return self.board
        else:
            return self.board[a]

    def get_board_solution(self):
        a: List[tuple[str, int, int]] = []
        for card in self.board:
            if card == None:
                pass
            else:
                a.append(card.get_card())
        return a

    def get_adjacencies(self):
        # ( placed card side, potential card side) index of placed card,
        # trbl = 0123
        adjacency_list: List[tuple[int, int, int], int] = (
            (None),  # 0
            ((0, self.right, self.left), None),  # 1
            ((1, self.right, self.left), None),  # 2
            ((0, self.bot, self.top), None),  # 3
            ((1, self.bot, self.top), (3, self.right, self.left)),  # 4
            ((2, self.bot, self.top), (4, self.right, self.left)),  # 5
            ((3, self.bot, self.top), None),  # 6
            ((4, self.bot, self.top), (6, self.right, self.left)),  # 7
            ((5, self.bot, self.top), (7, self.right, self.left)),  # 8
        )
        a = adjacency_list[self.next_open]
        if a == None:
            return
        for i in a:
            if i != None:
                yield i
            else:
                pass

    @property
    def next_open(self) -> int:
        return len(self.used_cards)

    def add_board_piece(self, a: Generic[T]) -> None:
        b: int = self.next_open

        # Set an initial piece
        if self.board[0] == None:
            self.board[0] = a
            self.used_cards.append(a.card_id)

        # Set non-initial pieces
        else:
            self.board[b] = a
            self.used_cards.append(a.card_id)

    def remove_board_piece(self):
        # make the last non-none board piece none
        self.board[len(self.used_cards) - 1] = None

        # remove the last card ID from the used list
        self.used_cards.pop()

    def solved(self, a: List[Card]) -> bool:
        return len(self.used_cards) == len(a)


class Card(object):

    card: str
    card_id: int
    card_ori: int

    def __init__(self, card, card_id, card_ori=0) -> None:
        self.card = card
        self.card_id = card_id
        self.card_ori = card_ori

    def rotate(self, r: List[int] = [1, 2, 3, 0]) -> Iterator[card]:
        if self.card_ori == 0:
            self.card = "".join(self.card[j] for j in r)
            self.card_ori = 1
        elif self.card_ori == 1:
            self.card = "".join(self.card[j] for j in r)
            self.card_ori = 2
        elif self.card_ori == 2:
            self.card = "".join(self.card[j] for j in r)
            self.card_ori = 3
        elif self.card_ori == 3:
            self.card = "".join(self.card[j] for j in r)
            self.card_ori = 0
        pass

    def all_rotations(self) -> Iterator[card]:
        for _ in range(4):
            self.rotate()
            yield

    def get_card(self) -> Tuple[str, int, int]:
        return self.card, self.card_id, self.card_ori

    def get_card_sides(self, a: int = None):
        if a == None:
            return self.card
        return self.card[a]


"""
Moving now into the non-class functions
and seeing if we can get this baby working.
"""


def edgecheck(a: str, b: str):
    c = a.isupper() ^ b.isupper()
    d = a.lower() == b.lower()
    if c and d:
        return True
    else:
        return False


def fits(board, card: str) -> bool:
    global xx
    global board_view
    board_view.update_board(card.card, board.get_board_solution())

    fits = [False, None]

    for ind, adj in enumerate(board.get_adjacencies()):

        a, b, c = [_ for _ in adj]
        x = edgecheck(board.get_board(a).get_card_sides(b), card.get_card_sides(c))

        # Check we haven't used the card before
        # z = card.card_id not in board.used_cards

        fits[ind] = x  # and z

    if False not in fits:
        return True
    else:
        return False


# Recursive search function
def find_next_card(board: Generic[T], potential_cards: List[Generic[T]]):
    global recursive_calls
    global xx
    recursive_calls += 1
    for card in potential_cards:
        if card.card_id not in board.used_cards:
            for _ in card.all_rotations():

                if fits(board, card):
                    board.add_board_piece(card)

                    if board.solved(potential_cards):
                        break
                    else:
                        find_next_card(board, potential_cards)
                        break

        # if board.solved(potential_cards):
        #     break

    if board.solved(potential_cards):
        return

    else:
        time.sleep(xx)
        board.remove_board_piece()

        if board.board[0] == None:
            return

        # find_next_card(board, potential_cards)


def solve(board: Generic[T], starting_cards: List[Card]) -> List[tuple[str, int, int]]:

    global board_view
    for card in starting_cards:
        # If the board is solved, return it and stop
        if board.solved(starting_cards):
            board_view.update_board(None, board.get_board_solution())
            print("Solution found:", board.get_board_solution())
            return

        # Else, search for the solution
        else:
            for _ in card.all_rotations():
                if board.solved(starting_cards):
                    return
                else:
                    # Make sure board is clear
                    board.clear_board()
                    # Set the first board piece
                    board.add_board_piece(card)

                    # Begin recursive search
                    find_next_card(board, starting_cards)


puzzle_input: List[str] = [
    "acdb",
    "ABCD",
    "Dadb",
    "AcbD",
    "cabd",
    "bCaA",
    "CBaD",
    "CdBc",
    "bacC",
]

test_puzzle_input: List[str] = [
    "acdb",
    "ABcD",
    "DadA",
]

# Create our list of Card class objects
xx = 0.00
solution = Board()
board_view = Show_board(xx)
parsed_cards: List[Generic[T]] = list()
recursive_calls = 0

for idx, card in enumerate(puzzle_input):
    parsed_cards.append(Card(card, idx))


if __name__ == "__main__":
    t1 = time.perf_counter()
    solve(solution, parsed_cards)
    t2 = time.perf_counter()
    t3 = t1 - t2
    print(f"{recursive_calls} recursive calls executed in {t2-t1} seconds")
