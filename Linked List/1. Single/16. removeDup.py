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
        swapped = True
        while swapped:
            swapped = False
            current = self.__head
            
            while current.get_next() is not None:
                if current.get_data() > current.get_next().get_data():
                    temp = current.get_data()
                    current.set_data(current.get_next().get_data())
                    current.get_next().set_data(temp)
                    swapped = True
                current = current.get_next()
    
    def list_nodes(self):
        current = self.__head
        
        while current is not None:
            print(current.get_data(), end='->')
            current = current.get_next()
        print('\n')
            

sll = SinglrLinkedList()

sll.push_nodes(10)
sll.push_nodes(20)
sll.push_nodes(40)
sll.push_nodes(30)
sll.push_nodes(60)
sll.push_nodes(70)
sll.push_nodes(50)

while True:
    print("---------------MENU-----------------")
    print("1.list nodes \n2.sort nodes \n3.exit")
    print("enter your option: ", end='')
    op = int(input())
    if op == 1:
        print()
        sll.list_nodes()
    elif op == 2:
        sll.sort_list()
    else:
        break
    
            
            
            