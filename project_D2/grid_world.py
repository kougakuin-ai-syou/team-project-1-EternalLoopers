import numpy as np

class GridWorld:
    def __init__(self, size=(4, 4), goal=(3, 3)):
        self.size = size
        self.goal = goal
        self.state = (0, 0)
        self.actions = ["up", "down", "left", "right"]

    def reset(self):
        self.state = (0, 0)
        return self.state

    def step(self, action):
        x, y = self.state
        if action == "up" and x > 0:
            x -= 1
        elif action == "down" and x < self.size[0] - 1:
            x += 1
        elif action == "left" and y > 0:
            y -= 1
        elif action == "right" and y < self.size[1] - 1:
            y += 1

        self.state = (x, y)
        reward = 1 if self.state == self.goal else -0.01
        done = self.state == self.goal
        return self.state, reward, done
