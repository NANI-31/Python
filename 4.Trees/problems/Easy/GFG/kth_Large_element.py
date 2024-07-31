from display import display
from print import printed

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def kth_largest(root, k):
    count = [0]
    return dfs(root, k, count)

def dfs(node, k, c):
    if not node: 
        return None
    right = dfs(node.right, k, c)
    if right: 
        return right
    c[0] += 1
    if c[0] == k: 
        return node.val
    return dfs(node.left, k, c)
        
        
root = Node(4) 
root.left = Node(2) 
root.right = Node(7) 
root.left.left = Node(1) 
root.left.right = Node(3) 
root.right.left = Node(6) 
root.right.right = Node(10) 

display(root)
k = 2
printed(f"{k} largest Node in BST is: {kth_largest(root, k)}")

