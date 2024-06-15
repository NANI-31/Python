class Node:
    def __init__(self):
        self.__data = 0
        self.__next = None
    def set_data(self,data):
        self.__data = data
    def get_data(self):
        return self.__data
    def set_next(self, data):
        self.__next = data
    def get_next(self):
        return self.__next

class Single:
    def __init__(self):
        self.__head = None
        
    def add_at_tail(self, data):
        p = Node()
        p.set_data(data)
        if self.__head is None:
            self.__head = p
        else:
            q = self.__head
            while q.get_next() is not None:
                q = q.get_next()
            q.set_next(p)
    
    def add_at_head(self, data):
        p = Node()
        p.set_data(data)
        if self.__head is None:
            self.__head = p
        else:
            q = self.__head
            p.set_next(q)
            self.__head = p
    
    def print_nodes(self):
        q = self.__head
        while q.get_next() is not None:
            print(q.get_data())
            q = q.get_next()
        
            
        


sll = Single()

while True:
    print("1.add at tail\n2.add at head\n3.print nodes\n")
    ch = int(input("enter the choice: "))
    if ch == 1:
        data = int(input("enter the data"))
        sll.add_at_tail(data)
    elif ch == 2:
        data = int(input("enter the data"))
        sll.add_at_head(data)
    elif ch == 3:
        sll.print_nodes()
    else:
        break
        
    