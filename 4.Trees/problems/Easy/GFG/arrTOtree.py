from display import display
from print import printed

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

def arrTOtree(arr):
    if not arr: return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = arrTOtree(arr[:mid])
    root.right = arrTOtree(arr[mid + 1:])
    return root

printed("converting array to Tree")
arr = [1,2,3,4,5,6,7]
printed("arr values: ",arr)
r = arrTOtree(arr)
display(r)
        