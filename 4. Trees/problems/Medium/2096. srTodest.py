#Leet Code 2096
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(node, val, path):
            if node.val == val:
                return True
            elif node.left and find(node.left, val, path):
                path.append('L')
            elif node.right and find(node.right, val, path):
                path.append('R')
            return path
        
        s = []
        d = []
        find(root, startValue, s)
        find(root, destValue, d)

        while len(s) and len(d) and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return 'U' * len(s) + ''.join(d[::-1])
        