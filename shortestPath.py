from queue import Queue
from constants import *
import threading
from heapq import *

# Recursive function that marks the shortest path in a certain color
# The animation starts from the starting node
def shortestPathHelper(node):

    # Base case
    # Executes once we reach the starting node
    if node.state == 'green':
        return

    shortestPathHelper(node.formerNode)

    if SHORTEST_PATH_ANIMATION:
        threading.Event().wait(REFRESH_RATE / 1000)

    if node.state != 'red':
        node.state = 'orange'

# Function that resets the searched nodes and gets the shortest path
def displayShortestPath(searchedNodes, maze):

    # Reset all nodes to white
    for node in searchedNodes:
        node.state = 'white'
    
    # Call recursive helper function
    shortestPathHelper(maze[NUMBER_OF_BLOCKS - 1][NUMBER_OF_BLOCKS - 1])

# Function that returns the manhattan distance from a node to the end
# This is a simple but efficient heuristic
def manhattanDistance(x, y):
    return 2 * NUMBER_OF_BLOCKS - x - y

def BFShelper(nodeQueue, currentNode, newNode):

    if not newNode.visited:
        newNode.formerNode = currentNode
        nodeQueue.put(newNode)

# Search algorithm based on priority queue
def BFS(maze, nodeQueue):

    searchedNodes = []

    while nodeQueue:

        node = nodeQueue.get()

        node.visited = True

        # Executed if we encounter the goal node
        if node.state == 'red':
            displayShortestPath(searchedNodes, maze)
            break

        # Changes a white node to a color to indicate that the node is being searched
        # This color indicates the head of BFS
        if node.state not in ['green', 'red']:
            node.state = 'blue'
            searchedNodes.append(node)

        if PATHFINDING_ANIMATION:
            threading.Event().wait(REFRESH_RATE / 1000)

        # Change the node to a color that represents the fact that it's been accounted for
        if node.state == 'blue':
            node.state = 'cyan'

        if node.up == False:
            upwardNode = maze[node.y - 1][node.x]

            BFShelper(nodeQueue, node, upwardNode)

        if node.down == False:
            downwardNode = maze[node.y + 1][node.x]

            BFShelper(nodeQueue, node, downwardNode)

        if node.left == False:
            leftwardNode = maze[node.y][node.x - 1]

            BFShelper(nodeQueue, node, leftwardNode)
        
        if node.right == False:
            rightwardNode = maze[node.y][node.x + 1]

            BFShelper(nodeQueue, node, rightwardNode)

def calculateHeuristic(pQueue, currentNode, newNode, count):

    if not newNode.visited:

        count[0] += 1

        newNode.formerNode = currentNode
        newNode.cost = currentNode.cost + 1
        cost = newNode.cost + manhattanDistance(newNode.x, newNode.y)
        costTuple = (cost, count[0], newNode)

        heappush(pQueue, costTuple)

def aStar(maze, pQueue):

    searchedNodes = []

    count = [0]
    
    while pQueue:

        node = heappop(pQueue)[2]
        node.visited = True

        # Executed if we encounter the goal node
        if node.state == 'red':
            displayShortestPath(searchedNodes, maze)
            break

        # Changes a white node to a color to indicate that the node is being searched
        # This color indicates the head of BFS
        if node.state not in ['green', 'red']:
            node.state = 'blue'
            searchedNodes.append(node)

        if PATHFINDING_ANIMATION:
            threading.Event().wait(REFRESH_RATE / 1000)

        # Change the node to a color that represents the fact that it's been accounted for
        if node.state == 'blue':
            node.state = 'cyan'
        
        if node.up == False:
            upwardNode = maze[node.y - 1][node.x]

            calculateHeuristic(pQueue, node, upwardNode, count)

        if node.down == False:
            downwardNode = maze[node.y + 1][node.x]

            calculateHeuristic(pQueue, node, downwardNode, count)

        if node.left == False:
            leftwardNode = maze[node.y][node.x - 1]

            calculateHeuristic(pQueue, node, leftwardNode, count)
        
        if node.right == False:
            rightwardNode = maze[node.y][node.x + 1]

            calculateHeuristic(pQueue, node, rightwardNode, count)


def getShortestPath(maze):
    
    # The starting node is at the top left corner
    startNode = maze[0][0]

    if SEARCH_ALGORITHM == 'BFS':

        nodeQueue = Queue()
        nodeQueue.put(startNode)

        BFS(maze, nodeQueue)
    
    if SEARCH_ALGORITHM == 'A*':

        startTuple = (0 + manhattanDistance(0, 0), 0, startNode)
        pQueue = []
        heappush(pQueue, startTuple)

        aStar(maze, pQueue)
