#! /usr/bin/python3
import time
import numpy as np


class Show_board:
    def __init__(self, slp, board=[]):
        self.board = board
        self.slp = slp

    def reset_board(self):
        r = "."
        matrix = [
            [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],
            [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],
            [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],
            [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],
            [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],
            [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],
            [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],
            [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],
            [r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],
        ]
        self.board = matrix

    def update_board(self, card, raw=[]):
        self.reset_board()

        solution = []
        time.sleep(self.slp)
        for i in raw:
            solution.append(i[0])

        if len(solution) != 9:
            solution.append(card)

        for i, e in enumerate(solution):
            # top row top side
            b = [0, 5, 10]
            c = [0, 3, 6]

            #              row              col
            self.board[0 + c[i // 3]][2 + b[i % 3]] = e[0]
            self.board[1 + c[i // 3]][0 + b[i % 3]] = e[3]
            self.board[1 + c[i // 3]][4 + b[i % 3]] = e[1]
            self.board[2 + c[i // 3]][2 + b[i % 3]] = e[2]

        print("\n" * 15)
        print(f"solution length: {len(solution)}")
        for i in self.board:
            print("".join(i))
        time.sleep(self.slp)
