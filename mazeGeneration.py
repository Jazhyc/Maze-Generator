import random
import threading

from constants import *
from classes import *
from shortestPath import getShortestPath
from mazeDisplay import updateAllNodes

# This function removes the borders of a node
# The direction specifies which border needs to be removed
def removeBorders(maze, i, j, direction):

    if direction == 'None':
        return

    if direction == 'up':
        maze[j][i].up = False
        maze[j - 1][i].down = False
        maze[j - 1][i].updateNodeGraphic

    if direction == 'right':
        maze[j][i].right = False
        maze[j][i + 1].left = False
        maze[j][i + 1].updateNodeGraphic

    if direction == 'down':
        maze[j][i].down = False
        maze[j + 1][i].up = False
        maze[j + 1][i].updateNodeGraphic

    if direction == 'left':
        maze[j][i].left = False
        maze[j][i - 1].right = False
        maze[j][i - 1].updateNodeGraphic

# Function that generates a maze
# The start is at the top left and end is the bottom right
def generateMaze(maze):

    for i in range(NUMBER_OF_BLOCKS):
        for j in range(NUMBER_OF_BLOCKS):
            maze[j][i] = Node(i, j)

    # Instantiate the start and end of the maze
    # These are the top left and bottom right corners
    maze[0][0].state = "green"
    maze[NUMBER_OF_BLOCKS - 1][NUMBER_OF_BLOCKS - 1].state = "red"

    i = random.randrange(0, NUMBER_OF_BLOCKS)
    j = random.randrange(0, NUMBER_OF_BLOCKS)

    # Generate Maze using DFS
    mazeDFS(maze[i][j], maze)

    updateAllNodes(maze)

    # Calculate and display the shortest path
    getShortestPath(maze)

# Maze generation using DFS
def mazeDFS(node, maze):

    actionStack = []
    actionStack.append(Action(node, "None"))

    while actionStack:

        action = actionStack.pop()
        node = action.node

        # If the node has already been used, then we should ignore it
        if node.generated:
            continue
        
        # Remove the required border and update the visuals of the node
        node.updateNodeGraphic()
        removeBorders(maze, node.x, node.y, action.direction)

        if node.state not in ['green', 'red']:
            node.state = 'orange'

        node.updateNodeGraphic()

        if GENERATION_ANIMATION:
            threading.Event().wait(REFRESH_RATE / 1000)

        if node.state == 'orange':
            node.state = 'white'
        
        node.updateNodeGraphic()

        # Mark the current node as generated
        node.generated = True

        # This is a list that contains the neighboring nodes that have not been generated by DFS
        # It is a list of actions that contain the node and the direction with respect to the original node
        neighbors = []

        # We put the inverse direction in Action
        if node.x - 1 >= 0 and not maze[node.y][node.x - 1].generated:
            neighbors.append(Action(maze[node.y][node.x - 1], 'right'))
        
        if node.x + 1 < NUMBER_OF_BLOCKS and not maze[node.y][node.x + 1].generated:
            neighbors.append(Action(maze[node.y][node.x + 1], 'left'))
        
        if node.y + 1 < NUMBER_OF_BLOCKS and not maze[node.y + 1][node.x].generated:
            neighbors.append(Action(maze[node.y + 1][node.x], 'up'))
        
        if node.y - 1 >= 0 and not maze[node.y - 1][node.x].generated:
            neighbors.append(Action(maze[node.y - 1][node.x], 'down'))

        while neighbors:

            action = neighbors.pop(random.randrange(0, len(neighbors)))

            # Due to the recursive nature of the program, the status of a node in the stack can change
            if action.node.generated == True:
                continue

            actionStack.append(action)