from display import display
from print import printed

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.right = None
        self.left = None
    
def gcd(a,b):
    if b == 0: return a
    return gcd(b, a%b)
  
def getMaxGCD(root, res):
    if not root: return 0
    lGCD = getMaxGCD(root.left, res)
    rGCD = getMaxGCD(root.right, res)
    if lGCD and rGCD:
        siblingsGCD = gcd(lGCD, rGCD)
        res[0] = max(res[0], siblingsGCD)
    if not root.left:
        return root.val
    else:
        gcd(root.val, lGCD)
        
def maxGCD(root):
    r = [0]
    getMaxGCD(root, r)
    return r[0] 
        
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(4)
root.left.right = Node(8)
root.right.left = Node(10)
root.right.right = Node(20)


