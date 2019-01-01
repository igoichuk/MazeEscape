import numpy as np
import random
from environment import Maze


class Agent:

    def __init__(self, alpha=0.15, explore=0.2):
        self.stateHistory = [((0, 0), 0)]
        self.alpha = alpha
        self.explore = explore
        self.G = {state: np.random.uniform(low=-1.0, high=-0.1) for state in Maze.getStateSpace()}

    def chooseAction(self, state, allowedActions):

        nextMove = None

        chance = np.random.random()
        if chance < self.explore:
            nextMove = random.choice(allowedActions)
        else:
            maxG = -10e15
            for action in allowedActions:
                newState = tuple(sum(x) for x in zip(state, action))
                if self.G[newState] >= maxG:
                    nextMove = action
                    maxG = self.G[newState]

        return nextMove

    def updateStateHistory(self, state, reward):
        self.stateHistory.append((state, reward))

    def learn(self):
        target = 0

        for prev, reward in reversed(self.stateHistory):
            self.G[prev] = self.G[prev] + self.alpha * (target - self.G[prev])
            target += reward

        self.stateHistory = []
        self.explore -= 10e-5

