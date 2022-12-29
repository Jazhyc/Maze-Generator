import tkinter as tk
import threading
import constants
from mazeGeneration import *
from mazeDisplay import *
from inputWindow import *

def main():

    input_window()

    # Creates a 2D array and passes it to the generateMaze daemon
    maze = [[0 for i in range(constants.NUMBER_OF_BLOCKS)] for j in range(constants.NUMBER_OF_BLOCKS)]

    # Creates a worker thread that runs parallel to the tkinter window
    mazeAnimation = threading.Thread(target=generateMaze, args=(maze,), daemon=True)
    mazeAnimation.start()

    # Create window and display the maze inside of it
    window = createWindow()
    displayMaze(maze, window)

if __name__ == "__main__":
    main()