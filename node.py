class Node:

    def __init__(self):
        self.left = True
        self.up = True
        self.right = True
        self.down = True
        self.visited = False
        self.state = "white"

class Action:

    def __init__(self, node, direction, newX, newY):
        self.node = node
        self.direction = direction
        self.newX = newX
        self.newY = newY