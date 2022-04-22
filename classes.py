# Class defintion for a node
# These are the squares in the maze
# The object contains information regarding which walls are active and the state of the node
class Node:

    def __init__(self):
        self.left = True
        self.up = True
        self.right = True
        self.down = True

        # Variable used for maze generation
        self.generated = False

        # Variable used for path finding
        self.visited = False

        self.state = "white"

# Class defintion for an action
# An action consists of both the selected node and the direction of the action
# Only used during maze generation
class Action:

    def __init__(self, node, direction, newX, newY):
        self.node = node
        self.direction = direction
        self.newX = newX
        self.newY = newY