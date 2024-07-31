from display import display
from print import printed

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def levelMax(res, root, level):
    if not root: return 
    if level == len(res): 
        res.append(root.val)
    else: 
        res[level] = max(res[level], root.val)
        
    levelMax(res, root.left, level+1)
    levelMax(res, root.right, level+1)

def largestValues(root):
    res = []
    levelMax(res, root, 0)
    return res
        
root = Node(4) 
root.left = Node(9) 
root.right = Node(2) 
root.left.left = Node(3)
root.left.right = Node(5)
root.right.right = Node(7)
display(root)
printed("largest values in each level are:")
printed(largestValues(root))

