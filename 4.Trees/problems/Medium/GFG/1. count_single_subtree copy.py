from display import display
from print import printed

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None
def dfs(root, c):
    if not root: return True
    
    l = dfs(root.left, c)
    r = dfs(root.right, c)
    
    if not l or not r: return False
    if root.left and root.val != root.left.val: return False
    if root.right and root.val != root.right.val: return False
    
    c[0] += 1
    return True
    
def countSingle(root):
    c = [0]
    dfs(root, c)
    return c[0]
    

root = Node(5)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(5)

display(root)
printed(f"Count of Single Valued Subtrees is: {countSingle(root)}")

