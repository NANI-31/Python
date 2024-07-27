class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val 
        self.next = next

def reverse_Between(head, left, right):

    curr = head
    l_point = None
    l_point_prev = None
    r_point = None
    r_point_next = None
    lc,rc = 1,1
    while curr is not None:
        if lc+1 == left:
            l_point = curr.next
            l_point_prev = curr
        elif rc == right:
            r_point = curr
            r_point_next = curr.next
        lc += 1
        rc += 1

        curr = curr.next

    
    curr = l_point
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next 
    l_point_prev.next = prev
    while r_point:
        r_point = r_point.next
    prev.next = r_point
    return head
        
    
    
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

head = create_list(values)
print("original:")
print_List(head)

reverse_Between(head, 2,6)
print("modified:")
print_List(head)
        