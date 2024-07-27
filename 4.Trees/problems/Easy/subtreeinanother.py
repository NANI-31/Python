from print import printed
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None

def isIdentical(r1, r2):
    if not r1 and not r2:
        return True
    if not r1 or not r2:
        return False
    if r1 and r2 and r1.val == r2.val:
        return isIdentical(r1.left, r2.left) and isIdentical(r1.right, r2.right)
    
def isSubtree(r1, r2):
    if not r2:
        return True
    if not r1:
        return False
    if isIdentical(r1, r2):
        return True
    
    return isSubtree(r1.left, r2) or isSubtree(r1.right, r2)


T = Node(26)
T.right = Node(3)
T.right.right = Node(3)
T.left = Node(10)
T.left.left = Node(4)
T.left.left.right = Node(30)
T.left.right = Node(6)


S = Node(10)
S.right = Node(6)
S.left = Node(4)
S.left.right = Node(30)

if isSubtree(T,S):
    printed("Tree 2 is subtree of Tree 1")
else:
    printed("Tree 2 is not a subtree of Tree 1")
    



