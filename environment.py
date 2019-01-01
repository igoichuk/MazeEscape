import numpy as np

actionSpace = [(-1, 0), (1, 0), (0, -1), (0, 1)]


class Maze:

    def __init__(self):
        self.maze = np.zeros((6, 6))
        self.maze[5, :5] = 1
        self.maze[:4, 5] = 1
        self.maze[2, 2:] = 1
        self.maze[3, 2] = 1
        self.maze[0, 0] = 2
        self.robotPosition = (0, 0)
        self.steps = 0
        self.allowedStates = self.constructAllowedStates()

    def printMaze(self):
        print('-----------------------------------------')
        for row in self.maze:
            for col in row:
                if col == 0:
                    print('', end='\t')
                elif col == 1:
                    print('X', end='\t')
                elif col == 2:
                    print('R', end='\t')
            print('\n')
        print('-----------------------------------------')

    def isAllowedMove(self, state, action):
        y = state[0] + action[0]
        x = state[1] + action[1]
        if y < 0 or x < 0 or y > 5 or x > 5:
            return False

        return self.maze[y, x] != 1

    def updateMaze(self, action):
        y, x = self.robotPosition
        self.maze[y, x] = 0
        y += action[0]
        x += action[1]
        self.robotPosition = (y, x)
        self.maze[y, x] = 2
        self.steps += 1

    def isGameOver(self):
        return self.robotPosition == (5, 5)

    def getStateAndReward(self):
        return self.robotPosition, self.giveReward()

    def giveReward(self):
        return 0 if self.robotPosition == (5, 5) else -1

    def constructAllowedStates(self):
        allowedStates = {}
        for y, row in enumerate(self.maze):
            for x, col in enumerate(row):
                allowedStates[(y, x)] = [action for action in actionSpace if self.isAllowedMove((y, x), action)]

        return allowedStates

