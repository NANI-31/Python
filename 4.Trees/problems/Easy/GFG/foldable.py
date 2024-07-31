from print import printed
class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None
        
def isFoldable(r):
    if not r:
        return True
    return dfs(root, root)
def dfs(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if dfs(p.left, q.right) and dfs(p.right, q.left):
        return True

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(5)


if isFoldable(root):
    printed("Tree is foldable")
else:
    printed("Tree is not foldable")
    



