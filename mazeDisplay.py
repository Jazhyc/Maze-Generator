import tkinter as tk
from constants import *

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
    
    window.after(REFRESH_RATE, drawCanvas, canvas, maze, window)
    

# Function that displays the maze on a tkinter canvas
def displayMaze(maze, window):

    canvas = tk.Canvas(window, bg="white", highlightthickness=1, highlightbackground="black")

    window.after(0, drawCanvas, canvas, maze, window)
                
    # The expand argument is a bool that determines if the canvas should expand to fit the window
    canvas.pack(fill=tk.BOTH, expand=1)

    # Infinite loop
    window.mainloop()