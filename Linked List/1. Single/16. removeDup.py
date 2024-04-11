class Node:
    def __init__(self):
        self.__data = 0
        self.__next = None
        
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data
    
    def set_next(self, data):
        self.__next = data
    def get_next(self):
        return self.__next
    
class SinglrLinkedList:
    def __init__(self):
        self.__head = None
    
    def push_nodes(self, data):
        p = Node()
        p.set_data(data)
        if self.__head == None:
            self.__head = p
        else:
            current = self.__head
            while current.get_next() is not None:
                current  = current.get_next()
            current.set_next(p)
            
    
    def sort_list(self):
        current = self.__head
        next = current.get_next() 
        while current is not None:
            if current.get_data() > next.get_data():
                temp = current.get_data()
                current.set_data(next.get_data())
                next.set_data(temp)
            next = next.get_next()
            current = current.get_next()
    
    def list_nodes(self):
        current = self.__head
        
        while current.get_next() is not None:
            print(current.get_data(), end='->')
            current = current.get_next()
            
            
            