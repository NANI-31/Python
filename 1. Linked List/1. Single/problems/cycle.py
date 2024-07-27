class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val 
        self.next = next

def cycle(head):
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow.val
    return None
        
    
    
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
    # curr.next = head.next
    return head

values = [1,2,3,4,5,6,7,8,9]

head = create_list(values)
print("original:")
print_List(head)

print(cycle(head))

        