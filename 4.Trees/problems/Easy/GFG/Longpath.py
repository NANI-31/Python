from display import display
from print import printed

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def height(root, a):
    if not root: return 0
    lh = height(root.left, a)
    rh = height(root.right, a)
    a[0] = max(a[0], 1 + lh + rh)
    return 1 + max(lh, rh)
          
def diameter(root):
    if not root: return 0
    a = [0]
    h = height(root,a)
    return a[0],h

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.right = Node(5)
root.left.right.right.left = Node(5)
display(root)
printed("Diameter of tree/ Longest path of tree:")
printed(diameter(root))
