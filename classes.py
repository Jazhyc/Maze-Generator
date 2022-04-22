# Class defintion for a node
# These are the squares in the maze
# The object contains information regarding which walls are active and the state of the node
class Node:

    def __init__(self, xPos, yPos):
        self.left = True
        self.up = True
        self.right = True
        self.down = True

        # Variable used for maze generation
        self.generated = False

        # Variable used for path finding
        self.visited = False

        self.state = "white"
        self.x = xPos
        self.y = yPos

        # Variable used to return the shortest path
        self.formerNode = None

        # This represents the number of steps needed to get from the start node to current node
        self.cost = 0


# Class defintion for an action
# An action consists of both the selected node and the direction of the action
# Only used during maze generation
class Action:

    def __init__(self, node, direction):
        self.node = node
        self.direction = direction