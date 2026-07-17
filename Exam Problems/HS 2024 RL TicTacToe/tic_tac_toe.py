from pickle import NONE
import numpy as np
import random
import matplotlib.pyplot as plt
from collections import defaultdict

# Tic Tac Toe board representation
class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.done = False
        self.winner = None

    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.board[0, 0] = 1
        self.board[0, 2] = 1
        self.board[0, 1] = -1
        self.board[1, 1] = -1
        self.done = False
        self.winner = None
        return np.copy(self.board)

    def get_available_actions(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    def step(self, action, player):
        if self.board[action] == 0:
            self.board[action] = player
            if self.check_winner(player):
                self.done = True
                self.winner = player
                return np.copy(self.board), 1 if player == 1 else -1, self.done
            elif len(self.get_available_actions()) == 0:
                self.done = True
                self.winner = 0
                return np.copy(self.board), 0, self.done
            else:
                return np.copy(self.board), 0, self.done
        else:
            raise ValueError("Invalid action!")

    def check_winner(self, player):
        for i in range(3):
            if np.all(self.board[i, :] == player) or np.all(self.board[:, i] == player):
                return True
        if self.board[0, 0] == player and self.board[1, 1] == player and self.board[2, 2] == player:
            return True
        if self.board[0, 2] == player and self.board[1, 1] == player and self.board[2, 0] == player:
            return True
        return False