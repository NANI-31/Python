class Node:
    def __init__(self):
        self.__data = 0
        self.__next = None
        self.__prev_next = None

    def set_data(self,data):
        self.__data = data
    def get_data(self):
        return self.__data
    
    def set_prev_next(self,data):
        self.__prev_next = data
    def get_prev_next(self):
        return self.__prev_next
    
    def set_next(self,data):
        self.__next = data
    def get_next(self):
        return self.__next
    
class DoubleLinledList:
    def __init__(self):
        self.__head = None
        
    def push(self, x):
        p = Node()
        p.set_data(x)

        if self.__head == None:
            self.__head = p
        else:
            q = self.__head
            while q.get_next() is not None:
                q = q.get_next()
            q.set_next(p) 
            p.set_prev_next(q)
        print("node added at tail\n")
    
    def list_nodes(self):
        if self.__head == None:
            print("list is empty\n")
        else:
            q = self.__head
            first_node = True  # Flag to track the last node
            while q is not None:
                if not first_node:
                    print(" <=> ", end='')  # Print '->' for all nodes except the last one
                print(q.get_data(), end='')
                first_node = False
                q = q.get_next()
            print('\n')
            
    def reverse_list(self):
        current = self.__head
        if current != None:
            addr = None
            while current is not None:
                next = current.get_next()
                current.set_next(addr)
                current.set_prev_next(next)
                addr = current
                current = next
            self.__head = addr
            
            
            
        else:
            print("the list is empty\n")

       


sll = DoubleLinledList()
sll.push(10)
sll.push(20)
sll.push(30)
sll.push(40)
sll.push(50)

while True:
    print("--------MENU--------")
    print("1.list nodes \n2.reverse the list \n3.exit")
    print("choose an option", end=" ")
    op = int(input())
    if op == 1:
        print()
        sll.list_nodes()
    elif op == 2:
        sll.reverse_list()
    else:
        break
