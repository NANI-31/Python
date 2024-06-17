class Node:
    def __init__(self):
        self.__value = 0
        self.__next = None
    
    def set_value(self, value):
        self.__value = value
    def get_value(self):
        return self.__value
    def set_next(self, next):
        self.__next = next
    def get_next(self):
        return self.__next
    
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def isEmpty(self):
        return self.front is None
    
    def enqueue(self, value):
        q = Node()
        q.set_value(value)
        
        if self.rear is None:
            self.front = self.rear = q
        else:
            self.rear.set_next(q)
            self.rear = q
        self.size += 1
        print(f"enqueued {value} to the queue\n")
    
    def dequeue(self):
        if self.isEmpty():
            return print("\nqueue is empty\n")
        d_val = self.front.get_value()
        self.front = self.front.get_next()
        
        if self.front is None:
            self.rear = None
        self.size -= 1
        print(f"\ndequeued {d_val} from the queue\n")
        
    def peek(self):
        if self.isEmpty():
            return print("\nqueue is empty cannot peek\n")
        print(f"\nfront of the queue is {self.front.get_value()}\n")
        
    def rearr(self):
        if self.isEmpty():
            return print("\nqueue is empty cannot rear\n")
        print(f"\nrear of the queue is {self.rear.get_value()}\n")
    
    def getSize(self):
        print(f"\nqueue size is {self.size}\n")
        
    def dispaly(self):
        if self.isEmpty():
            return print("\nqueue is empty\n")
        cur = self.front
        while cur:
            print(cur.get_value(), end=" ")
            cur = cur.get_next()
        print("\n")

queue = Queue()
while True:
    print("------queue MENU------\n1.enqueue\n2.dequeue\n3.peek\n4.rear\n5.size\n6.display\n7.exit")
    op = int(input("enter your choice:"))
    if op == 1:
        data = int(input("\nenter the data:"))
        queue.enqueue(data)
    elif op == 2:
        queue.dequeue()
    elif op == 3:
        queue.peek()
    elif op == 4:
        queue.rearr()
    elif op == 5:
        queue.getSize()
    elif op == 6:
        queue.dispaly()
    else:
        break