import numpy as np
import random

# actionSpace = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
actionSpace = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Agent:

    def __init__(self, states, alpha=0.15, explore=0.2):
        self.stateHistory = [((0, 0), 0)]
        self.alpha = alpha
        self.explore = explore
        self.G = {state: np.random.uniform(low=-1.0, high=-0.1) for state in states}

    def chooseAction(self, state, allowedMoves):

        nextMove = None

        chance = np.random.random()
        if chance < self.explore:
            nextMove = random.choice(allowedMoves)
        else:
            maxG = -10e15
            for action in allowedMoves:
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

