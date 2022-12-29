import tkinter as tk
import constants
from constants import WINDOW_HEIGHT, WINDOW_WIDTH

def update_number_of_blocks(number_of_blocks):

    constants.NUMBER_OF_BLOCKS = int(number_of_blocks)
    constants.BLOCK_SIZE = WINDOW_HEIGHT / constants.NUMBER_OF_BLOCKS

def update_refresh_rate(refresh_rate):
        constants.REFRESH_RATE = int(refresh_rate)

def update_algorithm(algorithm):
    constants.SEARCH_ALGORITHM = algorithm

def update_generation(animation):
    constants.GENERATION_ANIMATION = animation

def update_pathfinding(animation):
    constants.PATHFINDING_ANIMATION = animation

def terminateWindow(window, entries):

    # Call the function update_number_of_blocks to update the number of blocks from the first entry box
    update_number_of_blocks(entries[0].get())
    update_refresh_rate(entries[1].get())
    update_algorithm(entries[2].get())
    update_generation(entries[3].get())
    update_pathfinding(entries[4].get())

    window.destroy()

# Creates a function which generates a tkinter window to get some values from the user
def input_window():

    # Creates a tkinter window
    window = tk.Tk()

    # Set size of window
    window.geometry("275x250")

    # Sets the title of the window
    window.title("Maze Generator")

    # Creates a label that will be displayed in the window
    label = tk.Label(window, text="Maze Generator and Path finding Visualizer v1.1")
    # Places the label in the window
    label.pack(side=tk.TOP)

    # Begin displaying the label
    l1 = tk.Label(window, text="Number of Blocks")
    l1.pack()
    # Add text box to get the number of blocks, put some text to the left of the box
    block_input = tk.Entry(window, width = 10)
    # Center text in the box
    block_input.config(justify = tk.CENTER)
    block_input.insert(0, "10") # Default value is 10
    block_input.pack()

    # Put the refresh rate below the number of blocks
    l2 = tk.Label(window, text="Refresh Time (ms)")
    l2.pack()
    # Add text box to get the refresh rate, put some text to the left of the box
    refresh_input = tk.Entry(window, width = 10)
    # Center text in the box
    refresh_input.config(justify = tk.CENTER)
    refresh_input.insert(0, "10") # Default value is 0.01
    refresh_input.pack()

    # Create a label for algorithm selection
    l3 = tk.Label(window, text="Algorithm")
    l3.pack()
    # Create a drop down menu for algorithm selection
    algorithm = tk.StringVar(window)
    algorithm.set("A*") # Default value is Depth First Search
    algorithm_options = ["A*", "BFS"]
    algorithm_menu = tk.OptionMenu(window, algorithm, *algorithm_options)
    algorithm_menu.pack()

    # Add a boolean variable to determine if the generation animation should be displayed
    generation_animation = tk.BooleanVar()
    generation_animation.set(True)
    generation_animation_check = tk.Checkbutton(window, text="Generation Animation", variable=generation_animation)
    generation_animation_check.pack()

    # Add a boolean variable to determine if the pathfinding animation should be displayed
    pathfinding_animation = tk.BooleanVar()
    pathfinding_animation.set(True)
    pathfinding_animation_check = tk.Checkbutton(window, text="Pathfinding Animation", variable=pathfinding_animation)
    pathfinding_animation_check.pack()

    # Create a list to store all entries
    entries = [block_input, refresh_input, algorithm, generation_animation, pathfinding_animation]

    # Creates a button that will be displayed in the window
    button = tk.Button(window, text="Generate Maze", command=lambda: terminateWindow(window, entries))

    # Add a label for displaying the author's name
    author = tk.Label(window, text="Created by: Jeremias Ferrao")
    author.pack(side=tk.BOTTOM)

    # Places the button in the window
    button.pack(side=tk.BOTTOM)

    # Displays the window
    window.mainloop()

    # Returns the window
    return window