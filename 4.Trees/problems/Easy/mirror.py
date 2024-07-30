from display import display
from print import printed

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None
        
def mirror(root):
    if not root: return 
    else:
        temp = root
        mirror(root.left)
        mirror(root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
printed("before mirrored:")
display(root)
printed("after mirrored:")
mirror(root)
display(root)
