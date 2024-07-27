# Leet Code 101
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(p ,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            else:
                return dfs(p.left,q.right) and dfs(p.right, q.left)
        return dfs(root.left, root.right)


# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True 
#         queue=[root.left,root.right]
#         while queue:
#             left=queue.pop(0)
#             right=queue.pop(0)
#             #print(right.val)
#             if not left and not right :
#                 continue
#             if not left or not right:
#                 return False
#             if left.val!=right.val:
#                 return False
#             queue.extend([left.left,right.right])
#             queue.extend([left.right,right.left])
#         return True 