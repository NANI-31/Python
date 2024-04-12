class Node:
    def __init__(self):
        self.__data = 0
        self.__next = None
        
    def set_data(self, data):
        self.__data= data
    def get_data(self):
        return self.__data
    
    def set_next(self, next):
        self.__next = next
    def get_next(self):
        return self.__next
    
class CircularLinkedList:
    def __init__(self):
        self.__head = None
        
    def insert_at_tail(self, data):
        p = Node()
        p.set_data(data)
        if self.__head == None:
            self.__head = p
            p.set_next(p)
        else:           
            current = self.__head
            while True:
                current = current.get_next()
                if current.get_next() == self.__head:
                    break
            current.set_next(p)
            p.set_next(self.__head.get_next())


cll = CircularLinkedList()

while True:
    print("---------------MENU-----------------")
    print("1.insert")
    print("2.setect loop")
    op = int(input("enter your option: "))
    if op == 1:
        data = int(input("enter the data: "))
        cll.insert_at_tail(data)
    elif op == 2:
        break
                
        