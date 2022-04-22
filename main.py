import tkinter as tk
import threading
from constants import *
from mazeGeneration import *
from mazeDisplay import *

#! At 50 or more blocks this program will reach the default recursion limit

def main():

    # Creates a 2D array and passes it the generateMaze daemon
    maze = [[0 for i in range(NUMBER_OF_BLOCKS)] for j in range(NUMBER_OF_BLOCKS)]

    mazeAnimation = threading.Thread(target=generateMaze, args=(maze,), daemon=True)
    mazeAnimation.start()

    # Create window and make it prevent its size from being changed
    window = createWindow()

    displayMaze(maze, window)

if __name__ == "__main__":
    main()