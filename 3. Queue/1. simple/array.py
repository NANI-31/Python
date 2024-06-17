class Queue:
    def __init__(self):
        self.__queue = []
        
    def set_value(self, data):
        self.__queue.append(data)
    
    def del_value(self):
        return self.__queue.pop(0)
    
    def get_value(self):
        return self.__queue
    
    
    def enqueue(self, data):
        self.set_value(data)
        print(f"enqueued {data} to the queue\n")
        
    def dequeue(self):
        if self.isEmpty():
            print("\nQueue is empty cannot dequeue\n")
            return
        d_val = self.del_value()
        print(f"\ndequeued {d_val} from the queue\n")
    
    def peek(self):
        if self.isEmpty():
            print("\nqueue is empty Cannot peek\n")
            return 
        print(f"\nfront of the queue is {self.get_value()[0]}\n")
    
    def rear(self):
        if self.isEmpty():
            print("\nqueue is empty\n")
            return
        print(f"\nrear of the queue is {self.get_value()[-1]}\n")
        
    def isEmpty(self):
        return len(self.get_value()) == 0
    
    def getSize(self):
        print(f"\nqueue size is {len(self.get_value())}\n")
        
    def display(self):
        if self.isEmpty():
            print("\nqueue is empty\n")
            return
        print("queue values:")
        print(self.get_value())
        
queue = Queue()
while True:
    print("1.enqueu\n2.dequeue\n3.peek\n4.rear\n5.size\n6.dispaly\n7.exit")
    op = int(input("enter the choice:"))
    if op == 1:
        data = int(input("\nenter the value:"))
        queue.enqueue(data)
    elif op == 2:
        queue.dequeue()
    elif op == 3:
        queue.peek()
    elif op == 4:
        queue.rear()
    elif op == 5:
        queue.getSize()
    elif op == 6:
        queue.display()
    else:
        break
    