# Reinforcement learning for Tic Tac Toe

In this task, you must implement an agent that uses Q-learning to learn to play Tic Tac Toe. For simplicity, the agent plays first, plays X, and the board starts as

```
X O X
- O -
- - -
```

The dash denotes an empty cell.

The class `TicTacToe` in the file `tic_tac_toe.py` implements the functionality of the tic tac toe game. We recall how to play tic tac toe at the end of this file.

The class `QLearningAgent` in the file `q_learning.py` implements the functionality of Q-learning. The function `train` in `utils.py` implements the main loop of the Q-learning algorithm.

## Task

Implement one iterative step of the Q-learning algorithm by completing the method `learn` in the class `QLearningAgent`. It takes as input the following:

- **state**: A representation of the board. This is a numpy array describing the board. A 0 in the array denotes an empty cell. A 1 denotes a cell marked with a X and a -1 denotes a cell marked with an O.
- **action**: The action chosen by the agent. The action is just a tuple indicating the coordinates where the agent is going to place an X.
- **next_state**: The new state obtained after taking the action on the board and then letting the opponent take an action. After the agent places an X, we place an O on the board, following an optimal adversarial strategy.
- **reward**: The reward obtained. The reward is 1 if the agent wins, -1 if the agent loses, and 0 if the game still goes on.

The method must use this information to update the current estimate for Q(s, a) as prescribed by the Q-learning algorithm. These estimates are stored in the attribute `q_table`. For a state s and an action a, we store our estimate for Q(s, a) as follows:

- The state s is reshaped into a list of 9 entries and then mapped to a string. We call this resulting string state key k. This is done by the method `get_state_key`.
- We store our estimate for Q(s, a) in `q_table[k][a]`.

All what you need to calculate the Q-learning update formula is provided in the arguments of the function `learn`. The values for the learning rate α and the discount factor γ are set in the constructor of the class `QLearningAgent`.

## Evaluation

Your implementation is used to train an agent object of type `QLearningAgent`. Then this agent is used to play 100 games of Tic Tac Toe against a program that we implemented and that plays Tic Tac Toe optimally. If your agent plays optimally, then it can only tie against our program. After the 100 games, we count the number of draws. Your score is a linear interpolation between (0, 0) and (100, 7). That is, to get 7 points for this task, you must tie against our program in all games. Also, to get any amount of points, you must tie at least once against our program.

## Appendix: How to Play Tic Tac Toe

Tic Tac Toe is a simple game for two players, usually known as X and O. The game is played on a 3x3 grid. Here are the steps to play:

### Setup

- **Grid Preparation:** Draw a 3x3 grid, which means creating two vertical lines and two horizontal lines to form nine equal squares.

### Game Rules

- **Starting the Game:** Decide who will go first. The first player will be X, and the second player will be O.
- **Taking Turns:** Players take turns placing their mark (X or O) in an empty square on the grid.
- **Objective:** The goal is to be the first player to get three of their marks in a row. The row can be horizontal, vertical, or diagonal.

### Winning the Game

- **Win Condition:** The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins the game.
- **Draw Condition:** If all nine squares are filled and neither player has three in a row, the game is a draw.

### Example of Gameplay

1. Turn 1: Player X places an X in the center.
2. Turn 2: Player O places an O in the top-left corner.
3. Turn 3: Player X places an X in the bottom-right corner.
4. Turn 4: Player O places an O in the top-center.
5. Turn 5: Player X places an X in the top-right corner.
6. Turn 6: Player O places an O in the center-left.
7. Turn 7: Player X places an X in the bottom-left corner.
8. Turn 8: Player O places an O in the bottom-center.
9. Turn 9: Player X places an X in the center-right.
