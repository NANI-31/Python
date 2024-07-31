from display import display
from print import printed

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def inOrderSuccessor(root, node):
    if node.right: return minValue(node.right)
    succ = Node(None)
    while root:
        if root.val < node.val: root = root.right
        elif root.val > node.val:
            succ = root
            root = root.left
        else: break
    return succ
            
def minValue(node):
    curr = node
    while curr:
        if not curr.left: break
        curr = curr.left
    return curr
    
def insert(node, data):
    if not node: return Node(data)
    else:
        if data <= node.val:
            new = insert(node.left, data)
            node.left = new
        else:
            new = insert(node.right, data)
            node.right = new
        return node  

root = None
root = insert(root, 20)
root = insert(root, 8)
root = insert(root, 22)
root = insert(root, 4)
root = insert(root, 12)
root = insert(root, 10)
root = insert(root, 14)
temp = root.left.right 
succ = inOrderSuccessor( root, temp)

display(root)
if succ:
    printed(f"Inorder Successor of {temp.val} is {succ.val}")
else:
     printed("InInorder Successor doesn't exist")



