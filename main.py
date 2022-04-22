import tkinter as tk
import threading
from constants import *
from mazeGeneration import *
from mazeDisplay import *

def main():

    # Creates a 2D array and passes it to the generateMaze daemon
    maze = [[0 for i in range(NUMBER_OF_BLOCKS)] for j in range(NUMBER_OF_BLOCKS)]

    # Creates a worker thread that runs parallel to the tkinter window
    mazeAnimation = threading.Thread(target=generateMaze, args=(maze,), daemon=True)
    mazeAnimation.start()

    # Create window and display the maze inside of it
    window = createWindow()
    displayMaze(maze, window)

if __name__ == "__main__":
    main()