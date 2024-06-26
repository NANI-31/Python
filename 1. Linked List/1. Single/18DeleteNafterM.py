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
            
    def delete_nodes(self, m, n):
        current = self.__head
        # m_nodes = 1
        # n_nodes = 0
        # while current.get_next() is not None:
        #     print("1w")
        #     while m_nodes <= m:
        #         current = current.get_next()
        #         m_nodes += 1
        #         print("2w")
                
        #     while n_nodes <= n:
        #         if current.get_next() is None:
        #             break
        #         current.set_next(current.get_next().get_next())
        #         n_nodes += 1
        #         print("3w")
        #     m_nodes = 1
        #     n_nodes = 0
        while current:
            for count in range(1, m):
                if current is None:
                    break
                current = current.get_next()
            
            t = current.get_next()
            
            for count in range(1, n+1):
                if t is None:
                    break
                t = t.get_next()
                
            current.set_next(t)
            current = t                
                
            


sll = SingleLinledList()
sll.push(10)
sll.push(20)
sll.push(30)
sll.push(40)
sll.push(50)



while True:
    print("--------MENU--------")
    print("1.list nodes \n2.delete at nodes \n3.exit")
    print("choose an option", end=" ")
    op = int(input())

    if op == 1:
        print()
        sll.list_nodes()
    elif op == 2:
        m  = int(input("enter the m value: "))
        n  = int(input("enter the n value: "))
        sll.delete_nodes(m,n)
    else:
        break
