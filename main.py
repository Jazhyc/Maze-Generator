import numpy
import random, time
import tkinter as tk
import threading
from constants import *
from node import *

# Global variable to be used between threads
mazeGenerated = False

#! At 50 or more blocks this program will reach the default recursion limit

# This function removes the borders of a node
# The direction specifies which border needs to be removed
def removeBorders(maze, i, j, direction):

    if direction == 'up':
        maze[j][i].up = False
        maze[j - 1][i].down = False

    if direction == 'right':
        maze[j][i].right = False
        maze[j][i + 1].left = False

    if direction == 'down':
        maze[j][i].down = False
        maze[j + 1][i].up = False

    if direction == 'left':
        maze[j][i].left = False
        maze[j][i - 1].right = False

# Maze generation using DFS
def DFSgeneration(node, i, j, maze):

    if node.state not in ['green', 'red']:
        node.state = 'orange'

    threading.Event().wait(REFRESH_RATE / 1000)

    if node.state == 'orange':
        node.state = 'white'

    # Mark the current node as visited
    node.visited = True

    # This is a list that contains the neighboring nodes that have not been visited by DFS
    # It is a list of actions that contain the node and the direction with respect to the original node
    neighbors = []

    if i - 1 >= 0 and not maze[j][i - 1].visited:
        neighbors.append(Action(maze[j][i - 1], 'left', i - 1, j))
    
    if i + 1 < NUMBER_OF_BLOCKS and not maze[j][i + 1].visited:
        neighbors.append(Action(maze[j][i + 1], 'right', i + 1, j))
    
    if j + 1 < NUMBER_OF_BLOCKS and not maze[j + 1][i].visited:
        neighbors.append(Action(maze[j + 1][i], 'down', i, j + 1))
    
    if j - 1 >= 0 and not maze[j - 1][i].visited:
        neighbors.append(Action(maze[j - 1][i], 'up', i, j - 1))

    while neighbors:

        action = neighbors.pop(random.randrange(0, len(neighbors)))

        # Due to the recursive nature of the program, the status of a node in the stack can change
        if action.node.visited == True:
            continue

        removeBorders(maze, i, j, action.direction)

        DFSgeneration(action.node, action.newX, action.newY, maze)

        

# Function that generates a maze
# The start is at the top left and end is the bottom right
def generateMaze(maze):

    global mazeGenerated

    i = random.randrange(0, NUMBER_OF_BLOCKS)
    j = random.randrange(0, NUMBER_OF_BLOCKS)

    DFSgeneration(maze[i][j], i, j, maze)

    mazeGenerated = True

# Simple function that creates a tkinter window
def createWindow():
    window = tk.Tk()
    window.title("Maze")
    
    # This codeblock forces the window to be placed at the centre of the screen
    # Obtained from https://stackoverflow.com/questions/14910858/how-to-specify-where-a-tkinter-window-opens
    # get screen width and height
    ws = window.winfo_screenwidth() # width of the screen
    hs = window.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (WINDOW_WIDTH/2)
    y = (hs/2) - (WINDOW_HEIGHT/2)

    # set the dimensions of the screen 
    # and where it is placed
    window.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH, WINDOW_HEIGHT, x, y))


    window.focus_set()
    window.focus_force()
    window.resizable(False, False)

    return window

def drawCanvas(canvas, maze, window):

    global mazeGenerated

    canvas.delete("all")

    for i in range(NUMBER_OF_BLOCKS):
        for j in range(NUMBER_OF_BLOCKS):

            x1 = BLOCK_SIZE * i
            y1 = BLOCK_SIZE * j
            x2 = BLOCK_SIZE * (i + 1)
            y2 = BLOCK_SIZE * (j + 1)
            
            node = maze[j][i]

            if node.left:
                canvas.create_line(x1, y1, x1, y2, width=LINE_SIZE)
            
            if node.up:
                canvas.create_line(x1, y1, x2, y1, width=LINE_SIZE)
            
            if node.right:
                canvas.create_line(x2, y1, x2, y2, width=LINE_SIZE)
            
            if node.down:
                canvas.create_line(x1, y2, x2, y2, width=LINE_SIZE)

            # This line prints the color of the node
            # A green rectangle represents the start
            # A red rectangle represents the end
            canvas.create_rectangle(x1, y1, x2, y2, fill=f'{node.state}', outline='white')
    
    if not mazeGenerated:
        window.after(REFRESH_RATE, drawCanvas, canvas, maze, window)
    

# Function that displays the maze on a tkinter canvas
def displayMaze(maze, window):

    canvas = tk.Canvas(window, bg="white", highlightthickness=1, highlightbackground="black")

    window.after(0, drawCanvas, canvas, maze, window)
                
    # The expand argument is a bool that determines if the canvas should expand to fit the window
    canvas.pack(fill=tk.BOTH, expand=1)

    # Infinite loop
    window.mainloop()

def main():

    # Creates an array filled with nodes in which all edges are complete
    maze = [[Node() for i in range(NUMBER_OF_BLOCKS)] for j in range(NUMBER_OF_BLOCKS)]

    # Instantiate the start and end of the maze
    # These are the top left and bottom right corners
    maze[0][0].state = "green"
    maze[NUMBER_OF_BLOCKS - 1][NUMBER_OF_BLOCKS - 1].state = "red"

    mazeAnimation = threading.Thread(target=generateMaze, args=(maze,), daemon=True)
    mazeAnimation.start()

    # Create window and make it prevent its size from being changed
    window = createWindow()

    displayMaze(maze, window)

if __name__ == "__main__":
    main()