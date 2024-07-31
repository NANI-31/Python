from display import display
from print import printed

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def height(root):
    if not root: return 0
    return 1 + max(height(root.left), height(root.right))

def isBalance(root):
    if not root: 
        return True
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh - rh) <= 1: 
        return True
    return False
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(8)

display(root)
if isBalance(root): 
    printed("Tree is balanced")
else: 
    printed("Tree is not balanced")

