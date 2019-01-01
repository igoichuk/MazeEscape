import matplotlib.pyplot as plt

from environment import Maze
from agent import Agent


def game(maze, agent):
    while not maze.isGameOver():
        state, _ = maze.getStateAndReward()

        action = agent.chooseAction(state, maze.allowedStates[state])
        maze.updateMaze(action)
        state, reward = maze.getStateAndReward()
        agent.updateStateHistory(state, reward)

        if maze.steps > 1000:   # timeout
            maze.robotPosition = (5, 5)


def experiment(gamesCount, agent):

    moveHistory = []

    for i in range(gamesCount):
        if i % 1000 == 0:
            print(i)

        maze = Maze()
        game(maze, agent)
        agent.learn()

        moveHistory.append(maze.steps)

    return moveHistory


if __name__ == "__main__":

    states = [(y, x) for x in range(6) for y in range(6)]

    robot1 = Agent(states, alpha=0.1, explore=0.25)
    moveHistory1 = experiment(gamesCount=5000, agent=robot1)
    print(moveHistory1[::100])  # number of steps converges to 10

    robot2 = Agent(states, alpha=0.99, explore=0.25)
    moveHistory2 = experiment(gamesCount=5000, agent=robot2)
    print(moveHistory2[::100])  # also converges to 10 but slower

    plt.subplot(211)
    plt.semilogy(moveHistory1, 'b--')
    plt.legend(['alpha=0.1'])

    plt.subplot(212)
    plt.semilogy(moveHistory2, 'r--')
    plt.legend(['alpha=0.99'])

    plt.show()
