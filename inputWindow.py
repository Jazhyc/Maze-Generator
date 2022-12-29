import tkinter as tk
import constants
from constants import WINDOW_HEIGHT, WINDOW_WIDTH

def update_number_of_blocks(number_of_blocks):

    constants.NUMBER_OF_BLOCKS = int(number_of_blocks)
    constants.BLOCK_SIZE = WINDOW_HEIGHT / constants.NUMBER_OF_BLOCKS

# Creates a function which generates a tkinter window to get some values from the user
def input_window():
    
        # Creates a tkinter window
        window = tk.Tk()
    
        # Sets the title of the window
        window.title("Maze Generator")

        # Add text box to get the number of blocks
        block_input = tk.Entry(window, text="Number of blocks", width=50)

        # Update the number of blocks after the user presses enter
        block_input.bind("<Return>", lambda x: update_number_of_blocks(block_input.get()))

        block_input.pack()

        # Sets the size of the window
        window.geometry(str(WINDOW_WIDTH // 2) + 'x' + str(WINDOW_HEIGHT // 2))
    
        # Creates a label that will be displayed in the window
        label = tk.Label(window, text="Maze Generator")
    
        # Creates a button that will be displayed in the window
        button = tk.Button(window, text="Generate Maze", command=window.destroy)
    
        # Places the label in the window
        label.pack()
    
        # Places the button in the window
        button.pack()
    
        # Displays the window
        window.mainloop()
    
        # Returns the window
        return window