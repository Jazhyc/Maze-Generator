from queue import Queue
from constants import *
import threading

def shortestPathHelper(node):

    # Base case
    # Executes once we reach the starting node
    if node.state == 'green':
        return

    shortestPathHelper(node.formerNode)

    threading.Event().wait(REFRESH_RATE / 1000)

    if node.state != 'red':
        node.state = 'orange'

def displayShortestPath(searchedNodes, maze):

    # Reset all nodes to white
    for node in searchedNodes:
        node.state = 'white'
    
    # Call recursive helper function
    shortestPathHelper(maze[NUMBER_OF_BLOCKS - 1][NUMBER_OF_BLOCKS - 1])


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

        threading.Event().wait(REFRESH_RATE / 1000)

        # Change the node to a color that represents the fact that it's been accounted for
        if node.state == 'blue':
            node.state = 'cyan'

        if node.up == False:
            upwardNode = maze[node.y - 1][node.x]

            if not upwardNode.visited:
                upwardNode.formerNode = node
                nodeQueue.put(upwardNode)

        if node.down == False:
            downwardNode = maze[node.y + 1][node.x]

            if not downwardNode.visited:
                downwardNode.formerNode = node
                nodeQueue.put(downwardNode)

        if node.left == False:
            leftwardNode = maze[node.y][node.x - 1]

            if not leftwardNode.visited:
                leftwardNode.formerNode = node
                nodeQueue.put(leftwardNode)
        
        if node.right == False:
            rightwardNode = maze[node.y][node.x + 1]

            if not rightwardNode.visited:
                rightwardNode.formerNode = node
                nodeQueue.put(rightwardNode)          

def getShortestPath(maze):
    
    # The starting node is at the top left corner
    startNode = maze[0][0]

    nodeQueue = Queue()
    nodeQueue.put(startNode)

    BFS(maze, nodeQueue)