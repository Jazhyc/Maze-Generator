# Class definition for a NodeGraphic
# This is an object that keeps track of the various objects used to illustrate a node on the canvas
# This class is needed to drastically improve the performance of tkinter when displaying large mazes
class NodeGraphic:

    def __init__(self, rect, upBorder, rightBorder, downBorder, leftBorder, canvas):
        self.rect = rect
        self.upBorder = upBorder
        self.rightBorder = rightBorder
        self.downBorder = downBorder
        self.leftBorder = leftBorder
        self.canvas = canvas

    def markForRemoval(self):

        if self.rect:
            self.canvas.itemconfig(self.rect, tag='remove')
        
        if self.upBorder:
            self.canvas.itemconfig(self.upBorder, tag='remove')
        
        if self.rightBorder:
            self.canvas.itemconfig(self.rightBorder, tag='remove')
        
        if self.downBorder:
            self.canvas.itemconfig(self.downBorder, tag='remove')
        
        if self.leftBorder:
            self.canvas.itemconfig(self.leftBorder, tag='remove')

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

        # Variable that keeps track if the node has been rendered
        self.isNodeDisplayed = False

        # This represents the area on the maze that the node represents
        self.nodeGraphic = NodeGraphic(None, None, None, None, None, None)
    
    def updateNodeGraphic(self):
        self.isNodeDisplayed = False
        self.nodeGraphic.markForRemoval()


# Class defintion for an action
# An action consists of both the selected node and the direction of the action
# Only used during maze generation
class Action:

    def __init__(self, node, direction):
        self.node = node
        self.direction = direction