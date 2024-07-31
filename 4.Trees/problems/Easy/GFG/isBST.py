from display import display
from print import printed

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def isBST(root):
    if not root: return True
    if root.left and root.left.val > root.val: 
        return False
    if root.right and root.right.val < root.val: 
        return False
    if not isBST(root.left) or not isBST(root.right): 
        return False
    return True
        
root = Node(4)
root.left = Node(2)
root.right = Node(5)
# root.right.left = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)

display(root)
if isBST(root):
    printed("Tree is BST") 
else:
    printed("Tree is not a BST")

