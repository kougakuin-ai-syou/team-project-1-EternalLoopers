import numpy as np
import random

class QLearningAgent:
    def __init__(self, env, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.env = env
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = np.zeros((env.size[0], env.size[1], len(env.actions)))
        self.actions = env.actions

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        x, y = state
        return self.actions[np.argmax(self.q_table[x, y])]

    def update(self, state, action, reward, next_state):
        x, y = state
        a = self.actions.index(action)
        next_x, next_y = next_state
        best_next_q = np.max(self.q_table[next_x, next_y])
        self.q_table[x, y, a] += self.alpha * (
            reward + self.gamma * best_next_q - self.q_table[x, y, a]
        )

    def train(self, episodes=1000):
        for _ in range(episodes):
            state = self.env.reset()
            done = False
            while not done:
                action = self.choose_action(state)
                next_state, reward, done = self.env.step(action)
                self.update(state, action, reward, next_state)
                state = next_state

    def test_run(self):
        state = self.env.reset()
        path = [state]
        done = False
        while not done:
            x, y = state
            action_index = np.argmax(self.q_table[x, y])
            action = self.actions[action_index]
            state, _, done = self.env.step(action)
            path.append(state)
        print("テスト経路:", path)
