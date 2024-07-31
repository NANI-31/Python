from display import display
from print import printed

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def zigzag(root):
    if not root: return
    curr_level, next_level, r = [], [], []
    ltr = 1
    curr_level.append(root)
    while len(curr_level)>0:
        t = curr_level.pop()
        r.append(t.val)
        if ltr:
            if t.left: next_level.append(t.left)
            if t.right: next_level.append(t.right)
        else:    
            if t.right: next_level.append(t.right)
            if t.left: next_level.append(t.left)
        if len(curr_level) == 0:
            ltr = not ltr
            curr_level , next_level = next_level, curr_level    
    return r

root = Node(4) 
root.left = Node(9) 
root.right = Node(2) 
root.left.left = Node(3)
root.left.right = Node(5)
root.right.right = Node(7)

display(root)
printed("zig-zag traversal of binary tree is:")
printed(zigzag(root))

