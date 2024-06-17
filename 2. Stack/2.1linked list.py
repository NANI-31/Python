class Node:
    def __init__(self):
        self.__data = 0
        self.__next = None
    
    def set_data(self,data):
        self.__data = data
    def get_data(self):
        return self.__data
    def set_next(self, next):
        self.__next = next
    def get_next(self):
        return self.__next

class Stack:
    def __init__(self):
        self.__top = None
        self.__size = 0
    
    def push(self, data):
        p = Node()
        p.set_data(data)
        p.set_next(self.__top)
        self.__top = p
        self.__size += 1
        print(f"pushed {data} onto the stack\n")
        
    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return None
        popval = self.__top.get_data()
        self.__top = self.__top.get_next()
        self.__size -= 1
        print(f"\npooped {popval} from the stack\n")
        return popval
    
    def peek(self):
        if self.isEmpty():
            print("\nstack is empty\n")
            return None
        print("\ntop of the stack is", self.__top.get_data(),"\n")
        return self.__top.get_data()
    
    def isEmpty(self):
        return self.__top is None
    
    def getsize(self):
        return self.__size
    
    def display(self):
        if self.isEmpty():
            print("\nstack is empty\n")
            return None
        current = self.__top
        print("\nstack values:")
        while current:
            print(current.get_data())
            current = current.get_next()
        print()
    
    def get_size(self):
        print(f"\nsize of the stack is {self.__size}\n")
            
stack = Stack()
while True:
    print("----stack MENU----\n1.push\n2.pop\n3.peek\n4.display\n5.size\n6.exit")
    op = int(input("enter the choice: "))
    if op == 1:
        data = int(input("\nenter the value: "))
        stack.push(data)
    elif op == 2:
        stack.pop()
    elif op == 3:
        stack.peek()
    elif op == 4:
        stack.display()
    elif op == 5:
        stack.get_size()
    else:
        exit
         