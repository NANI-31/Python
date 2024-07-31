from display import display
from print import printed

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def noLeafNodes(root):
    if not root: return 0
    if not root.left and not root.right: return 1
    return noLeafNodes(root.left) + noLeafNodes(root.right)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(5)
root.left.left.left = Node(8)

display(root)
printed(f"number of leaf nodes: {noLeafNodes(root)}") 


