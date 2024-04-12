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
    def get_head(self):
        return self.__head
    
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
            
    def merge_nodes(self, p, q):
        p_curr = p.get_head()
        q_curr = q.get_head()
        
        while p_curr != None and q_curr != None:
            p_next = p_curr.get_next()
            q_next = q_curr.get_next()
            
            q_curr.set_next(p_next)
            p_curr.set_next(q_next)
            
            q_curr = p_next
            q_curr = q_next
            q.set_head(q_curr) 
        

            


sll1 = SingleLinledList()
sll2 = SingleLinledList()
for i in range(1, 10, 2): 
    sll2.push(i) 
for i in range(20, 30, 2): 
    sll2.push(i) 



while True:
    print("--------MENU--------")
    print("1.list nodes \n2.list nodes \n3.list nodes \n4.Merge Lists \n5.exit")
    print("choose an option", end=" ")
    op = int(input())

    if op == 1:
        print()
        sll1.list_nodes()
    elif op == 2:
        print()
        sll1.list_nodes()
    elif op == 3:
        print()
        sll2.list_nodes()
    elif op == 4:
        print()
        sll1.merge_nodes(p=sll1, q=sll2)
    else:
        break
