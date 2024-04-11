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
    
    def Nth_Node_from_end(self, value):
        if value == 0:
            return
        q = self.__head
        p = None
        last_occ_addr = None
        while q is not None:
            if value == q.get_data():
                last_occ_addr = p
            p = q
            q = q.get_next()
            
        if last_occ_addr is None and self.__head.get_data() == value:
            self.__head = self.__head.get_next()
            
        elif last_occ_addr is not None:
            if last_occ_addr.get_next() is not None:
                last_occ_addr.set_next(last_occ_addr.get_next().get_next())
            else:
                p.set_next(None)

            
        
        
            
            
            
        
        
        




        
       


sll = SingleLinledList()
sll.push(10)
sll.push(20)
sll.push(30)
sll.push(40)
sll.push(50)
sll.push(10)
sll.push(70)



while True:
    print("--------MENU--------")
    print("1.list nodes \n2.delete last occurence \n5.exit")
    print("choose an option", end=" ")
    op = int(input())

    if op == 1:
        print()
        sll.list_nodes()
    elif op == 2:
        sll.Nth_Node_from_end(10)
    else:
        break
