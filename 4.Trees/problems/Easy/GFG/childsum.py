from display import display
from print import printed

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def childSum(root):
    if not root: return True
    if not root.left and not root.right: return True
    lcv = root.left.val if root.left else 0 
    rcv = root.right.val if root.right else 0 
    if root.val != lcv + rcv: return False
    return childSum(root.left) and childSum(root.right)
    
root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.right = Node(2)
root.right.left = Node(2)

display(root)
t = "The given tree satisfies the children sum property "
f = "The given tree does not satisfy the children sum property "
printed(t) if childSum(root) else printed(f)


