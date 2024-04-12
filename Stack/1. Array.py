class Satck:
    def __init__(self):
        self.__stack = []
        self.__max_size = 0
    
    def set_stack(self, data):
        self.__stack.append(data)
    def get_stack(self):
        return self.__stack
    
    def set_maxsize(self, data):
        self.__max_size = data
    def get_maxsize(self):
        return self.__max_size
    
    def is_empty(self):
        return len(self.get_stack()) == 0
    
    def is_full(self):
        if self.get_maxsize() is None:
            return False
        return len(self.get_stack() >= self.get_maxsize)
    
    def push(self, item):
        if self.is_full():
            print("stack overflow")
            return
        self.set_stack(item)
        print("pushed", item, "into the stack")
        
    def pop(self):
        if self.is_empty():
            print("stack underflow")
            return None
        item = self.get_stack().pop()
        print("popped", item, "from the stack")
        return item
    
    def peek(self):
        if self.is_empty():
            print("stack is empty")
            return None
        return self.get_stack()[-1]
    
    def size(self):
        return len(self.get_stack())
    

stack = Satck()
print("set the size of stack")
s_size = int(input())
stack.set_maxsize(s_size)
while True:
    print("---------------MENU------------------")
    print("1. push")
    print("2. pop")
    print("3. peek")
    print("4. exit")
    
    op = input("enter your choice")
    
    if op == '1':
        data = int(input())
        stack.push(data)
    elif op == '2':
        data = stack.pop()
    elif op == '3':
        data = stack.peek()
        if data is not None:
            print("top element of the stack:", data)
    elif op == '4':
        break
        
    