class Node:
    def __init__(self, val=0, next=None) -> None:
        self.val = val 
        self.next = next

def reverse(head):
    a = []
    curr = head
    while curr:
        if curr.val % 2 == 0:
            a.append(curr.val)
        curr = curr.next
    a.reverse()
    curr = head
    index = 0
    while curr:
        if curr.val % 2 == 0:
            curr.val = a[index]
            index += 1
        curr = curr.next
    
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

reverse(head)
print("modified:")
print_List(head)
        