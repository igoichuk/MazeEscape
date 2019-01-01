from environment import Maze
from agent import Agent
from main import game


if __name__ == "__main__":

    robot = Agent()

    maze = Maze()
    maze.printMaze()

    game(maze, robot)

    print(maze.steps)

