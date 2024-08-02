from display import display
from print import printed
 
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inOrderTravel(root):
    inOrder, s = [], []
    while True:
        if root:
            s.append(root)
            root = root.left
        else:
            if not s: break
            root = s.pop()
            inOrder.append(root.val)
            root = root.right
    return inOrder

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(8)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(9)
root.right.right.right = Node(10)

inOrder = inOrderTravel(root)
printed("The inOrder Traversal is : ")
printed(inOrder)
# for data in inOrder:
#     printed(data)