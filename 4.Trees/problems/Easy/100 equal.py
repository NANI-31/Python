# Leet code 100
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
# # Just three conditions we have to check!
#         def dfs(node1, node2):

#             # 1. Do we have both nodes? If so, are they equal? 
#             # If yes, continue recursion; else, return false.
#             if node1 and node2:
#                 if node1.val != node2.val:
#                     return False
#                 else:
#                     return dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            
#             # 2. Are both nodes None? If so, we can return True.
#             elif not node1 and not node2:
#                 return True
            
#             #3. Is any one node None? If so, return False. It's not the same tree.
#             else:
#                 return False

#         return dfs(p, q)


# ==========================================================================================


# def isSameTree(self, p, q):
#         stack = [(p, q)]
#         while stack:
#             (p, q) = stack.pop()
#             if p and q and p.val == q.val:
#                 stack.append((p.left,  q.left))
#                 stack.append((p.right, q.right))
#             elif p or q:
#                 return False
#         return True