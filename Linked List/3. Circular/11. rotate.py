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

        if self.__head == None:
            self.__head = p
            p.set_next(p)
        else:
            q = self.__head
            while True:
                q = q.get_next()
                if q.get_next() == self.__head:
                    break
            q.set_next(p)
            p.set_next(self.__head)
            self.__head = p
        print("node added at head\n")
        

    
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
    print("1.list nodes \n6.exit")
    print("choose an option", end=" ")
    op = int(input())

    if op == 1:
        print()
        sll.list_nodes() 
    elif op == 2:
        print()
        sll.list_nodes()
    else:
        break
