import tkinter as tk
from constants import *
from classes import NodeGraphic

# Simple function that creates a tkinter window
def createWindow():
    window = tk.Tk()
    window.title("Maze")

    # Destroy window on escape
    window.bind("<Escape>", lambda x: window.destroy())
    
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

# Function that tells the canvas to update the visuals of all nodes
def updateAllNodes(maze):
    for i in range(NUMBER_OF_BLOCKS):
        for j in range(NUMBER_OF_BLOCKS):
            maze[j][i].updateNodeGraphic()

def drawCanvas(canvas, maze, window):

    # Only remove the objects that are marked for removal
    canvas.delete("remove")

    for i in range(NUMBER_OF_BLOCKS):
        for j in range(NUMBER_OF_BLOCKS):

            x1 = BLOCK_SIZE * i
            y1 = BLOCK_SIZE * j
            x2 = BLOCK_SIZE * (i + 1)
            y2 = BLOCK_SIZE * (j + 1)
            
            node = maze[j][i]

            if not node.isNodeDisplayed:

                # This line prints the color of the node
                # A green rectangle represents the start
                # A red rectangle represents the end
                rect = canvas.create_rectangle(x1, y1, x2, y2, fill=f'{node.state}', outline=f'{node.state}')

                leftBorder = None
                upBorder = None
                rightBorder = None
                downBorder = None

                if node.left:
                    leftBorder = canvas.create_line(x1, y1, x1, y2, width=LINE_SIZE)
                
                if node.up:
                    upBorder = canvas.create_line(x1, y1, x2, y1, width=LINE_SIZE)
                
                if node.right:
                    rightBorder = canvas.create_line(x2, y1, x2, y2, width=LINE_SIZE)
                
                if node.down:
                    downBorder = canvas.create_line(x1, y2, x2, y2, width=LINE_SIZE)

                node.nodeGraphic = NodeGraphic(rect, upBorder, rightBorder, downBorder, leftBorder, canvas)

                node.isNodeDisplayed = True
    
    if not shortest_path_found:
        window.after(max(REFRESH_RATE, 1), drawCanvas, canvas, maze, window)
    

# Function that displays the maze on a tkinter canvas
def displayMaze(maze, window):

    canvas = tk.Canvas(window, bg="white", highlightthickness=1, highlightbackground="black")

    window.after(0, drawCanvas, canvas, maze, window)
                
    # The expand argument is a bool that determines if the canvas should expand to fit the window
    canvas.pack(fill=tk.BOTH, expand=1)

    # Infinite loop
    window.mainloop()