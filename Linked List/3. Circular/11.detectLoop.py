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
    
    def get_head(self):
        return self.__head
        
    def push(self, data):
        p = Node()
        p.set_data(data)
        if self.__head == None:
            self.__head = p
            p.set_next(p)
        else:
            current = self.__head
            while current.get_next() != self.__head:
                current = current.get_next()
            current.set_next(p)
            p.set_next(self.__head)

        
    def printList(self):
        temp = self.__head
        while True:
            print(temp.get_data(), end=" ")
            temp = temp.get_next()
            if temp == self.__head:
                break
        print("\n")
            
    def detect_loop(self):
        s = set()
        t = 0
        current = self.__head
        while current:
            if current in s:
                t = 1
                break
            s.add(current)
            current = current.get_next()
        
        print("loop found") if t else print("no loop")
        
  


cll = CircularLinkedList()
cll.push(10)
cll.push(20)
cll.push(30)
cll.push(40)
cll.push(50)

# cll.get_head().get_next().get_next().get_next().set_next(cll.get_head())

while True:
    print("---------------MENU-----------------")
    print("1.print listinsert")
    print("2.detect loop")
    op = int(input("enter your option: "))
    if op == 1:
        print()
        cll.printList()
    elif op == 2:
        cll.detect_loop()
    else:
        break
                
        