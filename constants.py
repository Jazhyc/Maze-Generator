# These variables determine the size of the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# This variable determines the number of blocks in the maze
NUMBER_OF_BLOCKS = 20

# We obtain the size of block by dividing the height of the window by the number of blocks
BLOCK_SIZE = WINDOW_HEIGHT / NUMBER_OF_BLOCKS

# How much time should pass before the next action takes place
REFRESH_RATE = 100

# This is how thick the walls of the maze should look like
LINE_SIZE = 6

# Search algorithm to be used
SEARCH_ALGORITHM = 'A*'