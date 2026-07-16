import random
import numpy as np
from test_utils import optimal_opponent_action

# Training the agent
def train(agent, env, episodes=10000):
    for episode in range(episodes):
        # print("Episode start")
        state = env.reset()
        done = False
        while not done:
            old_state = np.copy(state)
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action, 1)
            # agent.learn(state, action, reward, next_state)
            state = next_state
            # print(next_state)
            if done:
                break
            # Opponent's turn
            if len(env.get_available_actions()) > 0:
                opponent_action = optimal_opponent_action(env.board)
                next_state, reward, done = env.step(opponent_action, -1)
                if done:
                    reward = -1
                    agent.learn(old_state, action, reward, next_state)
                else:
                    agent.learn(old_state, action, reward, next_state)
                state = next_state
            # print(next_state)

# Evaluation
def play_game(agent, env):
    state = env.reset()
    done = False
    while not done:
        action = agent.choose_action(state)
        state, reward, done = env.step(action, 1)
        if done:
            break
        if len(env.get_available_actions()) > 0:
            opponent_action = random.choice(env.get_available_actions())
            state, reward, done = env.step(opponent_action, -1)
    return env.winner