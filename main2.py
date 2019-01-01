from environment import Maze
from agent import Agent


def game(maze, agent):
    while not maze.isGameOver():
        state, _ = maze.getStateAndReward()

        action = agent.chooseAction(state, maze.allowedStates[state])
        maze.updateMaze(action)
        state, reward = maze.getStateAndReward()
        agent.updateStateHistory(state, reward)

        if maze.steps > 1000:
            maze.robotPosition = (5, 5)


if __name__ == "__main__":

    states = ((y, x) for x in range(6) for y in range(6))

    robot1 = Agent(states, alpha=0.15, explore=0.2)
    maze = Maze()

    maze.printMaze()

    game(maze, robot1)

    print(maze.steps)

