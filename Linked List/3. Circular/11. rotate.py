class Node:
    def __init__(self):
        self.__data = 0
        self.__next = None

    def set_data(self,data):
        self.__data = data
    def get_data(self):
        return self.__data
    
    def set_next(self,data):
        self.__next = data
    def get_next(self):
        return self.__next
    
class CircularLinledList:
    def __init__(self):
        self.__head = None
    
    def push(self, data):
        p = Node()
        p.set_data(data)
        p.set_next(self.__head)
        self.__head = p
        

    
    def list_nodes(self):
        if self.__head == None:
            print("list is empty\n")
        else:
            q = self.__head
            first_node = True  # Flag to track the last node
            while True:
                if not first_node:
                    print(" -> ", end='')  # Print '->' for all nodes except the last one
                print(q.get_data(), end='')
                first_node = False
                q = q.get_next()
                if q == self.__head:
                    break
            print('\n')

        

       


sll = CircularLinledList()

for i in range(60, 0, -10): 
    sll.push(i) 

while True:
    print("--------MENU--------")
    print("1.add at tail \n2.add at head \n3.Add in position(btw) \n4.list nodes \n6.exit")
    print("choose an option", end=" ")
    op = int(input())

    if op == 1:
        print("\nenter the data:", end=" ")
        data = int(input())
        sll.add_at_tail(data)
    elif op == 2:
        print("\nenter the data:", end=" ")
        data = int(input())
        sll.add_at_head(data)
    elif op == 3:
        print("\nenter the data:", end=" ")
        data = int(input())
        print("enter the position:", end=" ")
        pos = int(input())
        sll.add_at_position(data, pos) 
    elif op == 4:
        print()
        sll.list_nodes()
    elif op == 5:
        sll.print_middle_values()
    else:
        break
