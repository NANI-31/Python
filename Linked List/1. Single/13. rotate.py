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
    
class SingleLinledList:
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
        print("node added at head\n")
    
    def list_nodes(self):
        if self.__head == None:
            print("\nlist is empty\n")
        else:
            q = self.__head
            first_node = True  # Flag to track the last node
            while q is not None:
                if not first_node:
                    print(" -> ", end='')  # Print '->' for all nodes except the last one
                print(q.get_data(), end='')
                first_node = False
                q = q.get_next()
            print('\n')
    
    def rotate_list(self, k):
        if k == 0:
            return
        count = 1
        q = self.__head
        initial_addr = q
        while count < k and q.get_next() is not None:
            q = q.get_next()
            count += 1
        print(q.get_data()) 
        if q is None: 
            return
        
        self.__head = q.get_next()
        q.set_next(None)
        p = self.__head
        
        while p.get_next() is not None:
            p = p.get_next()
        p.set_next(initial_addr)
            
            
        
        
        




        
       


sll = SingleLinledList()
sll.push(10)
sll.push(20)
sll.push(30)
sll.push(40)
sll.push(50)
sll.push(60)


while True:
    print("--------MENU--------")
    print("1.list nodes \n2.rotate list \n5.exit")
    print("choose an option", end=" ")
    op = int(input())

    if op == 1:
        print()
        sll.list_nodes()
    elif op == 2:
        sll.rotate_list(4)
    else:
        break
