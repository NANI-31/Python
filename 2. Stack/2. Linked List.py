class Node:
    def __init__(self):
        self.__data = 0
        self.__next = None
    
    def set_data(self,data):
        self.__data= data
    def get_data(self):
        return self.__data
    
    def set_next(self, next):
        self.__next = next
    def get_next(self):
        return self.__next
    
class Stack:
    def __init__(self):
        self.__top = None
        
    def is_empty(self):
        return self.__top is None
    
    def push(self, data):
        p = Node()
        p.set_data(data)
        if self.is_empty():
            self.__top = p
        else:
            p.set_next(self.__top)
            self.__top = p
        
    def pop(self):
        if self.is_empty():
            print("stack underflow")
            return None
        else:
            top_element = self.__top.get_data()
            self.__top = self.__top.get_next()
            return  top_element
    
    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return None
        else:
            return self.__top.get_data()
    
    def display_stack(self):
        if self.is_empty():
            print("stack is empty")
        else:
            current = self.__top
            while current:
                print(current.get_data())
                current = current.get_data()
                
                
                
stack = Stack()

while True:
    print("-------------MENU---------------")
    print("1. Push")                
    print("2. Pop")                
    print("3. Peek")                
    print("4. dispaly")                
    print("5. exit")   
    
    op = int(input("eneter your option: "))
    
    if op == 1:
        element = int(input("eneter the element to push: "))
        stack.push(element)     
    elif op == 2:
        stack.pop()
    elif op == 3:
        stack.peek()
    elif op == 4:
        stack.display_stack()
    else: 
        break        

            
            
        
    
    