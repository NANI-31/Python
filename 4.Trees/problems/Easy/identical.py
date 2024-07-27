from print import printed
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None
        
def isIdentical(r1, r2):
    if not r1 and not r2:
        return True
    if r1 and r2 and r1.val == r2.val:
        return isIdentical(r1.left, r2.left) and isIdentical(r1.right, r2.right)
    else:
        return False 


root1 = Node(1)
root2 = Node(1)

root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

if isIdentical(root1, root2):
    printed("Both trees are identical")
else:
    printed("Trees not are identical")
    



