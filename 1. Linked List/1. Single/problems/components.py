class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val 
        self.next = next

def components(head, nums):
    c = 0
    while head.next:
        print(head.val, head.next.val)
        if head.val in nums and head.next.val in nums:
            head = head.next
            c += 1
    if head.val in nums:
        c += 1
    return c

def print_List(head):
    while head:
        print(head.val,end = " -> ")
        head = head.next
    print("None")
        
        
def create_list(values):
    head = Node(values[0])
    curr = head
    for value in values[1:]:
        curr.next = Node(value)
        curr = curr.next
    return head

values = [1,2,3,4,5,6,7,8,9]
nums = [0,1,3]
head = create_list(values)
print("original:")
print_List(head)

print(components(head, nums))

        