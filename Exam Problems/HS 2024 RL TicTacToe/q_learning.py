from collections import defaultdict
import numpy as np
import random

# Q-learning Agent
class QLearningAgent:
    def __init__(self, alpha=0.1, gamma=0.9, epsilon=0.3):
        np.random.seed(41)
        random.seed(41)
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = defaultdict(lambda: np.zeros((3, 3)))

    def get_state_key(self, state):
        return str(state.reshape(9))

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            available_actions = [(i, j) for i in range(3) for j in range(3) if state[i, j] == 0]
            return random.choice(available_actions)
        else:
            return self.make_move(state)
            
    def make_move(self, state):
        state_key = self.get_state_key(state)
        state_values = self.q_table[state_key]
        masked_state_values = np.where(state == 0, state_values, -np.inf)
        best_action = np.unravel_index(np.argmax(masked_state_values), (3, 3))
        return best_action

    # TASK: Complete this method!
    def learn(self, state, action, reward, next_state):
        state_key = self.get_state_key(state)
        next_state_key = self.get_state_key(next_state)
        # ...